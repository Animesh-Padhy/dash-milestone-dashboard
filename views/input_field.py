import dash_bootstrap_components as dbc
from dash import dcc,html
import dash
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

LAYOUT_STYLE = {
    'padding':'1rem 1rem',
    'background-color':'rgb(20,25,250)',
    'border-style':'context',
    'fontSize':'100%'
}

input_table_header = [html.Thead(html.Tr(html.Th('User Input')))]
labels = [
    'Latitude:*',
    "Longitude:*",
    'Data:*',
    'Country:*',
]
input_id = [
    'lat',
    'long',
    'input-dataset',
    'input-value'
]
placeholder = [
    'Latitude Eg. - 39.6491',
    'Longitude Eg. - 79.992',
    'Enter dataset GDP vs (country or year)',
    'Enter a country name'
]

rows_input = []
for i,j,k in zip(labels, input_id, placeholder):
    if '*' in i:
        if 'Latitude' in i:
            rows_input.append(
                html.Tr(
                    [
                        html.Td([i]),
                        html.Td(
                            [
                                dbc.Input(
                                    type = 'number',
                                    id = j,
                                    placeholder = k,
                                    min = -90,
                                    max = 90,
                                    required = 'required',
                                )
                            ],
                            style = {'padding':'10px'}
                        ),
                    ]
                )
            )
        elif 'Longitude' in i:
            rows_input.append(
                html.Tr(
                    [
                        html.Td([i]),
                        html.Td(
                            [
                                dbc.Input(
                                    type = 'number',
                                    id = j,
                                    placeholder = k,
                                    min = -180,
                                    max = 180,
                                    required = 'required',
                                )
                            ],
                            style = {'padding':'10px'}
                        ),
                    ]
                )
            )
        elif 'Data' in i:
            rows_input.append(
                html.Tr(
                    [
                        html.Td([i]),
                        html.Td(
                            [
                                dbc.Input(
                                    type = 'text',
                                    id = j,
                                    placeholder = k,
                                    required = 'required',
                                )
                            ],
                            style = {'padding':'10px'}
                        ),
                    ]
                )
            )
        elif 'Country' in i:
            rows_input.append(
                html.Tr(
                    [
                        html.Td([i]),
                        html.Td(
                            [
                                dbc.Input(
                                    type = 'text',
                                    id = j,
                                    placeholder = k,
                                    required = 'required',
                                )
                            ],
                            style = {'padding':'10px'}
                        ),
                    ]
                )
            )

input_table_body = [html.Tbody(rows_input)]

input_table = dbc.Table(
    input_table_header + input_table_body, responsive=True, hover=True
)

calculated_table_body = [html.Tbody(id='cal_body')]

calculated_table = dbc.Table(
    [html.Thead(html.Tr([html.Th('Calculated Output')]))] + calculated_table_body,
    responsive = True,
    hover = True,
)

modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader('Sheetz'),
                dbc.ModalBody(id = 'popupmsg'),
                # dbc.ModalFooter(
                #     dbc.Button(
                #         'Close',id='close',className='ms-auto',n_clicks=0
                #     )
                # ),
            ],
            id = 'modal',
            is_open = False,
        )
    ]
)

layout = html.Div(
    [
        dcc.Loading(
            id = 'loading-2',
            children=[
                dbc.Row(
                    [
                        #popup box
                        modal,
                        #user inputs
                        dbc.Row(
                            [input_table],
                            className = 'col-md-6',
                        ),
                        #calculated outputs
                        dbc.Col(
                            [
                                calculated_table
                                # dcc.Loading(
                                #     id = 'loading-2',
                                #     children = [html.Div([calculated_table])],
                                #     type='circle',
                                # )
                            ],
                            className = 'col-md-6',
                        ),
                        # dcc.Loading(
                        #     type = 'circle',
                        #     children = []
                        # ),

                        # Button to redirect to simulate 
                        dbc.Col(
                            [
                                dbc.Button(
                                    children = 'Simulate',
                                    id = 'simulate',
                                    color = 'primary',
                                    className = 'me-1',
                                    n_clicks = 0,
                                    style = {
                                        'font-size':'20px',
                                        'text-decoration':'none',
                                    },
                                )
                            ],
                            className = 'col-md-12',
                            style={'text-align':'center','padding':'20px'},
                        ),
                    ],
                    className = 'container-fluid',
                ),
            ],
            type = 'circle',
        ),

        # Product variety start
    ]
)


input_field_list = [Output(i,'value') for i in input_id] + [
    # Output('cal_body','children')
]

# output_values = [Output(i,'children') for i in calculated_id]
input_values = [State(i,'value') for i in input_id]
output_values = [
    Output('modal','is_open'),
    Output('popupmsg','children'),
    Output('calculated_table_vals','data'),
    Output('scenario_df','data'),
    Output('calculated_map_fig','data'),
    Output('scenario_id','data'),
]

if __name__ == '__main__':
    app.layout = layout  
    app.run_server(debug=True)