from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl


map = dl.Map(
    dl.TileLayer(),
    id="map-output",
    center=[20, 20],  # default values
    zoom=6,
    style={
        "height": 400,
        "width": "95%",
        "margin": "auto",
        "marginTop": "30px",
    },
)

simulation_layout = html.Div(
    children=[
        map,
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Label(
                            "User Provided Fields",
                            className="userProvidedField",
                            style={"fontWeight": "bold"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div(
                                            children=[
                                                dbc.Label(
                                                    "Latitude: ",
                                                    className="header",
                                                    style={"fontWeight": "bold"},
                                                ),
                                                dbc.Input(
                                                    valid="",
                                                    id="latitude1",
                                                    disabled=True,
                                                ),
                                            ],
                                            className="UserInput",
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            children=[
                                                dbc.Label(
                                                    "Longitude: ",
                                                    className="header",
                                                    style={"fontWeight": "bold"},
                                                ),
                                                dbc.Input(
                                                    valid="",
                                                    id="longitude1",
                                                    disabled=True,
                                                ),
                                            ],
                                            className="UserInput",
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            children=[
                                                dbc.Label(
                                                    "Data: ",
                                                    className="header",
                                                    style={"fontWeight": "bold"},
                                                ),
                                                dbc.Input(
                                                    valid="",
                                                    id="data1",
                                                    disabled=True,
                                                ),
                                            ],
                                            className="UserInput",
                                        ),
                                        html.Hr(),
                                        html.Div(
                                            children=[
                                                dbc.Label(
                                                    "Country: ",
                                                    className="header",
                                                    style={"fontWeight": "bold"},
                                                ),
                                                dbc.Input(
                                                    valid="",
                                                    id="country1",
                                                    disabled=True,
                                                ),
                                            ],
                                            className="UserInput",
                                        ),
                                        html.Hr(),
                                    ],
                                    className="formContainer",
                                )
                            ]
                        ),
                        html.Div(children="Output generated"),
                    ],
                    style={
                        "width": "50%",
                        "display": "inline-block",
                        "verticalAlign": "top",
                        "margin": "10px",
                    },
                ),
                html.Div(
                    children=[
                        html.Label(
                            "Country Data: ",
                            className="userProvidedField",
                            style={"fontWeight": "bold"},
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Label(
                                            "Total GDP: ",
                                            style={"fontWeight": "bold"},
                                        ),
                                        html.Span(id="totalgdpSim"),
                                    ],
                                    className="countryItem",
                                ),
                                html.Hr(),
                                html.Div(
                                    children=[
                                        html.Label(
                                            "Total Population: ",
                                            style={"fontWeight": "bold"},
                                        ),
                                        html.Span(id="totalpopSim"),
                                    ],
                                    className="countryItem",
                                ),
                                html.Hr(),
                                html.Div(
                                    children=[
                                        html.Label(
                                            "Average life Expectancy: ",
                                            style={"fontWeight": "bold"},
                                        ),
                                        html.Span(id="avgExpSim"),
                                    ],
                                    className="countryItem",
                                ),
                                html.Hr(),
                            ],
                            className="countryclass",
                        ),
                    ],
                    style={
                        "width": "40%",
                        "display": "inline-block",
                        "verticalAlign": "top",
                        "margin": "10px",
                    },
                ),
            ],
            className="inputandcountry",
            style={"width": "95%", "margin": "auto", "marginTop": "30px"},
        ),
        # Bar Chart 
        html.Div(
            children=[
                html.Label(
                    "Calculated Bar Chart",
                    className="userProvidedField calculatedBarChart",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "20px",
                        "textAlign": "center",
                        "display": "block",
                    },
                ),
                html.Div(
                    children=[dcc.Graph(id="bar-chart")],
                    className="calculatedBarChart",
                    style={"width": "80%", "margin": "auto"},
                ),
            ],
            style={"textAlign": "center", "marginTop": "30px"},
        ),
        # Country Bar Chart 
        html.Div(
            children=[
                html.Label(
                    " ",
                    id="headingOfChart",
                    className="userProvidedField calculatedBarChart",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "20px",
                        "textAlign": "center",
                        "display": "block",
                    },
                ),
                html.Div(
                    children=[dcc.Graph(id="country-bar-chart")],
                    className="calculatedBarChart",
                    style={"width": "80%", "margin": "auto"},
                ),
            ]
        ),
    ],
    id="simulation",
)


def simulationLayout():
    return simulation_layout
