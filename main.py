import dash
from dash import Dash, html, dcc, Input, Output, callback, State
import dash_bootstrap_components as dbc
from flask import Flask
from flask_login import LoginManager, UserMixin, login_user
from views.callbacks import allCallbacks
from dash.exceptions import PreventUpdate
import sqlite3

server = Flask(__name__)
server.config.update(SECRET_KEY="MY_SECRET_KEY")

app = Dash(
    __name__,
    server=server,
    use_pages=False,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)

login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = "/login"


class User(UserMixin):
    def __init__(self, username):
        self.id = username


@login_manager.user_loader
def load_user(username):
    return User(username)


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About", href="/about", style={"color": "white"})),
        dbc.NavItem(
            dbc.NavLink("Input Field", href="/inputField", style={"color": "white"})
        ),
        dbc.NavItem(
            dbc.NavLink("Simulation", href="/simulation", style={"color": "white"})
        ),
        dbc.NavItem(dbc.NavLink("Logout", href="/logout", style={"color": "white"})),
    ],
    color='primary',
    style={"background-color": "#007bff", "margin-bottom": "20px","width":"90%"},
)


app.layout = html.Div(
    children=[
        dcc.Store(id="session", storage_type="session"),
        dcc.Location(id="url", refresh=False),
        dcc.Location(id="redirect", refresh=True),
        html.Div(
            children=[
                html.Div(
                html.Img(src="assets/tiger_analytics_img.png", className="company_logo",
                style={'height': '47px','width': '100%',} 
                )),
                navbar,
            ],
            style={'display':'flex','justify-content':'left','background-color':'primary'},
            className="topNav_container",
        ),
        html.Div(id="page-content"),
    ],
),


@app.callback(
    Output("redirect", "pathname"),
    Output("incorrectCredentials", "children"),
    Input("loginUser", "n_clicks"),
    [State("usernameField", "value"), State("passwordField", "value")],
    prevent_initial_call=True,
)
def checkLogin(n_clicks, userName, password):
    if not n_clicks:
        raise PreventUpdate

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    query = (
        "SELECT name,password FROM users where name= '"
        + userName
        + "' and password='"
        + password
        + "'"
    )
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()

    if len(results) != 0:
        user = User(userName)
        login_user(user)
        return "/about", dash.no_update
    else:
        return "/login", "Incorrect Credentials. Try Again"


allCallbacks()

if __name__ == "__main__":
    app.run(debug=True)
