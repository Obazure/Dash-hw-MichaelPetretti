import dash
import dash_core_components as dcc
import dash_html_components as html

from src.views.components import upload_file, select_file, load_and_represent_data

"""Create a dashboard app with Dash."""
layout = html.Div(
    children=[
        dcc.Store(id='storage-report-file-loaded', storage_type='session'),
        dcc.Store(id='storage-selected-report', storage_type='session'),
        dcc.Store(id='storage-selected-attributes', storage_type='session'),

        html.Div(className='mt-5 mb-5', children=[
            html.H4('Step 1. Add new report:'),
            upload_file.layout
        ]),
        html.Div(className='mt-5 mb-5', children=[
            html.H4('Step 2. Find uploaded report or select existing to plot:'),
            select_file.layout
        ]),
        html.Div(className='mt-5 mb-5', children=[
            html.H4('Step 3. Review report:'),
            load_and_represent_data.layout
        ]),
    ])
