# navbar

import dash_bootstrap_components as dbc
# from core.utils.ui_constants import HEADER_STYLE
from dash import html


style_nav_bar_inactive = {
    'fontSize':'100%',
    'text-decoration':'none',
    'textAlign':'center',
    'color':'#fff',
    'backgroundColor':'#0062d1',
}

style_nav_bar_active = {
    'font-weight':'bold',
    'fontSize':'100%',
    'color':'#fff',
    'textAlign':'center',
    'backgroundColor':'#0700d1',
}

def get_header(active_page = 'success'):
    l1_nav = [
        ('About',''),
        ('Input Filed','scenario_planner'),
        ('Simulation','simulation'),
    ]
    nav_list = []
    for index_, value_ in enumerate(l1_nav):
        nav_list.append(
            dbc.NavLink(
                value_[0],
                href = "/" + value_[1],
                active='exact',
                style = style_nav_bar_active
                if value_[1] == active_page
                else style_nav_bar_inactive,
            )
        )
    
    header = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Nav(
                            [
                                html.Img(),
                                html.Div(
                                    [""],
                                    style={
                                        'margin-left':'15px',
                                        'margin-top':
                                        '9px',
                                        'fontweight':'bold',
                                    },
                                ),
                            ],
                            horizontal='start'
                        ),
                        width = 4,
                    ),
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavLink(
                                    'Logout',
                                    id = 'logout',
                                    href = '/logout',
                                    style = style_nav_bar_inactive,
                                    external_link = True,
                                ),
                            ],
                            vertical = False,
                            pills = True,
                            horizontal = 'end',
                        ),
                        align='center',
                    ),
                ],
                style = {
                    'background-color':'#0062d1',
                    'textAlign':'center',
                    'fontSize':'16px',
                    'color':'white',
                },
            ),
            html.Br(),
        ]
    )
    return header

header_logout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Nav(
                        [
                            html.Img(),
                        ],
                        horizontal = 'start',
                    ),
                ),
            ]
        ),
    ],
    # style = HEADER_STYLE
)

