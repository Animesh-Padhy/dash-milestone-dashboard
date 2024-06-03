import dash
import dash_table
import dash_html_components as html
import json
import pandas as pd
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback

with open('core/conf/config_about.json', 'r') as file:
    tables = json.load(file)

df = pd.read_csv('data/gapminderDataFiveYear.csv')
df = df[['continent', 'country', 'pop', 'lifeExp']]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = html.Div(
    children=[
        dbc.Row([html.H2('Introduction to Gapminder')], style={'text-align': 'center'}),
        dbc.Row([html.P(tables['intro_part1'])]),
        dbc.Row(
            [
                html.Ol(
                    [
                        html.Li(tables['intro_part1_list1']),
                        html.Li(tables['intro_part1_list2']),
                        html.Li(tables['intro_part1_list3']),
                        html.Li(tables['intro_part1_list4']),
                    ]
                )
            ]
        ),
        dbc.Label('Show number of rows'),
        row_drop := dcc.Dropdown(value=10, clearable=False, style={'width': '35%'}, options=[{'label': x, 'value': x} for x in [10, 25, 50, 100]]),
        my_table := dash_table.DataTable(
            columns=[
                {'name': 'Continent', 'id': 'continent', 'type': 'text'},
                {'name': 'Country', 'id': 'country', 'type': 'text'},
                {'name': 'Population', 'id': 'pop', 'type': 'numeric'},
                {'name': 'Life Expectancy', 'id': 'lifeExp', 'type': 'numeric'},
            ],
            data=df.to_dict('records'),
            filter_action='native',
            page_size=10,
            style_data={
                'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
                'overflow': 'hidden', 'textOverflow': 'ellipsis',
            }
        ),
        dbc.Row([
            dbc.Col([
                continent_drop := dcc.Dropdown([x for x in sorted(df.continent.unique())], placeholder='Select Continent')
            ], width=3),
            dbc.Col([
                country_drop := dcc.Dropdown([x for x in sorted(df.country.unique())], multi=True, placeholder='Select Country')
            ], width=3),
            dbc.Col([
                pop_slider := dcc.Slider(0, 1500000000, 5000000, marks={'1000000000': '1 billion', '1500000000': '1.5 billion'}, value=0, tooltip={'placement': 'bottom', 'always_visible': True})
            ], width=3),
            dbc.Col([
                lifeExp_slider := dcc.Slider(0, 100, 1, marks={'100': '100'}, value=20, tooltip={'placement': 'bottom', 'always_visible': True})
            ], width=3),
        ], justify='between', className='mt-3 mb-4'),
    ]
)

@app.callback(
    Output(my_table, 'data'),
    Output(my_table, 'page_size'),
    Input(continent_drop, 'value'),
    Input(country_drop, 'value'),
    Input(pop_slider, 'value'),
    Input(lifeExp_slider, 'value'),
    Input(row_drop, 'value')
)
def update_dropdown_options(cont_v, country_v, pop_v, life_v, row_v):
    dff = df.copy()

    if cont_v:
        dff = dff[dff.continent == cont_v]
    if country_v:
        dff = dff[dff.country.isin(country_v)]

    dff = dff[(dff['pop'] >= pop_v) & (dff['pop'] < 1500000000)]
    dff = dff[(dff['lifeExp'] >= life_v) & (dff['lifeExp'] < 100)]

    return dff.to_dict('records'), row_v

if __name__ == '__main__':
    app.layout = layout  
    app.run_server(debug=True)
