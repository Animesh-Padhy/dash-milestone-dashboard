from dash import html, dcc, dash_table
import pandas as pd
import json


def get_JsonData():
    file = open("conf/config_about.json")
    json_data = json.load(file)
    return json_data


dfr = pd.read_csv("data/gapminderDataFiveYear.csv")
df = dfr[["continent", "country", "pop", "lifeExp"]]

table = dash_table.DataTable(id="table", data=df.to_dict("records"), page_size=15)

pageSize_dropdown = html.Div(
    children=[
        html.Label("Select Page Size"),
        dcc.Dropdown(options=[10, 15, 20], value=10, id="page_dropdown"),
    ]
)

continent_dropdown = html.Div(
    children=[
        dcc.Dropdown(
            options=[
                {"label": cont, "value": cont} for cont in df["continent"].unique()
            ],
            value="",
            id="continent_dropdown",
            placeholder="Select Continent",
        )
    ]
)

country_dropdown = html.Div(
    children=[
        dcc.Dropdown(
            options=[
                {"label": country, "value": country}
                for country in df["country"].unique()
            ],
            value="",
            id="country_dropdown",
            placeholder="Select country",
        )
    ]
)

population_rangeSlider = html.Div(
    children=[
        dcc.RangeSlider(
            min=df["pop"].min(),
            max=df["pop"].max(),
            value=[df["pop"].min(), df["pop"].max()],
            id="population_slider",
        )
    ]
)

lifeExp_rageSlider = html.Div(
    children=[
        dcc.RangeSlider(
            min=df["lifeExp"].min(),
            max=df["lifeExp"].max(),
            value=[df["lifeExp"].min(), df["lifeExp"].max()],
            id="lifeExp_slider",
        )
    ]
)

about_layout = html.Div(
    children=[
        # Intro 
        html.Div(
            children=[
                html.H3(
                    children="Introduction to GapMinder",
                    className="intro-heading",
                    style={"text-align": "center", "margin": "auto", "width": "60%"},
                ),
                html.Div(
                    children=[
                        html.P(children=get_JsonData()["intro_part1"]),
                        html.Ol(
                            children=[
                                html.Li(children=get_JsonData()["intro_part1_list1"]),
                                html.Li(children=get_JsonData()["intro_part1_list2"]),
                                html.Li(children=get_JsonData()["intro_part1_list3"]),
                                html.Li(children=get_JsonData()["intro_part1_list4"]),
                            ],
                            className="intro-list",
                        ),
                    ],
                    className="intro-content",
                ),
            ],
            className="intro-section",
            style={"text-align": "left", "margin-left": "1rem", "width": "90%"},
        ),
        # Page Size Dropdown
        html.Div(
            children=[pageSize_dropdown],
            className="page-size-section",
        ),
        # Table
        html.Div(
            children=[table],
            className="table-section",
            style={"width": "100%"},
        ),
        # Filters
        html.Div(
            children=[
                html.Div(
                    children=[continent_dropdown],
                    className="filter-item",
                    style={"width": "24%", "margin": "0 1%"},
                ),
                html.Div(
                    children=[country_dropdown],
                    className="filter-item",
                    style={"width": "24%", "margin": "0 1%"},
                ),
                html.Div(
                    children=[population_rangeSlider],
                    className="filter-item",
                    style={"width": "24%", "margin": "0 1%"},
                ),
                html.Div(
                    children=[lifeExp_rageSlider],
                    className="filter-item",
                    style={"width": "24%", "margin": "0 1%"},
                ),
            ],
            className="filters-container d-flex",
            style={"justify-content": "space-between"},
        ),
        # Download Button
        html.Div(
            children=[
                html.Button(
                    children="Download CSV",
                    id="download_CSV",
                    className="btn btn-primary",
                ),
                dcc.Download(id="download"),
            ],
            className="download-section",
        ),
    ],
    className="about-layout",
)


def getUpdatedDataFrame(continent, country, popValue, lifeExpValue):
    dataFrame = df.copy(deep=True)
    if not continent and not country and not popValue and not lifeExpValue:
        return dataFrame.to_dict("records")

    if continent:
        dataFrame = dataFrame[dataFrame["continent"] == continent]

    if country:
        dataFrame = dataFrame[dataFrame["country"] == country]

    dataFrame = dataFrame[
        (popValue[0] <= dataFrame["pop"]) & (dataFrame["pop"] <= popValue[1])
    ]
    dataFrame = dataFrame[
        (lifeExpValue[0] <= dataFrame["lifeExp"])
        & (dataFrame["lifeExp"] <= lifeExpValue[1])
    ]
    return dataFrame


def dataFrame():
    return dfr


def aboutlogout():
    return about_layout
