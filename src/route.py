import dash
import dash_core_components as dcc
import dash_html_components as html

from src.views import error_page, main_page


def route(app):
    """App Routing by Url"""
    app.layout = html.Div(
        children=[
            dcc.Location(id='url', refresh=False),
            html.Nav(
                className='navbar navbar-expand-lg navbar-light bg-light',
                children=[
                    html.Div(className='container', children=[
                        dcc.Link('Alcemy', className='navbar-brand', href='/'),
                    ])
                ]
            ),
            html.Div(
                className='container',
                children=[
                    html.H1("Welcome to Dash Plot Visualization for CSV Reports!", className='text-center'),
                    html.Div(id='page-content')
                ]
            )
        ])

    @app.callback(
        dash.dependencies.Output('page-content', 'children'),
        [dash.dependencies.Input('url', 'pathname')]
    )
    def display_page(pathname):
        if pathname == '/':
            return main_page.layout
        return error_page.layout
