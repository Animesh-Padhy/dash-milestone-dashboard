from dash import html
import dash_bootstrap_components as dbc

login_layout = html.Div(
    children=[
        html.Label("Login", style={"fontSize": "xx-large"}),
        html.Div(
            children=[
                html.Div(
                    children=[
                        dbc.Label("Username*", className="username"),
                        dbc.Input(placeholder="username", id="usernameField"),
                    ],
                    className="loginForm",
                    style={
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "column-gap": "1rem",
                        "width": "500px",
                    },
                ),
                html.Div(
                    children=[
                        dbc.Label("Password*", className="password"),
                        dbc.Input(
                            placeholder="password", id="passwordField", type="password"
                        ),
                    ],
                    className="loginForm",
                    style={
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "column-gap": "1rem",
                        "width": "500px",
                    },
                ),
                html.Button(
                    "Login",
                    className="btn btn-primary",
                    id="loginUser",  
                    style={"width": "200px"},
                ),
            ],
            style={
                "display": "flex",
                "flexDirection": "column",
                "rowGap": "1rem",
                "alignItems": "center",
            },
        ),
        html.Div(id="incorrectCredentials"),
    ],
    className="loginPage",
    style={
        "text-align": " center",
        "display": "flex",
        "flex-direction": "column",
        "row-gap": "2rem",
    },
)


logout_layout = html.Div(
    children=[
        html.Div("You are logged out"),
        dbc.Button(children="Login", href="/login"),
    ]
)


def logoutLayout():
    return logout_layout


def loginLayout():
    return login_layout
