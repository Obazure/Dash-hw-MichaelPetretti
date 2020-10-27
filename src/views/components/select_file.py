import glob
from pathlib import Path

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from config.config import STORAGE_DIRECTORY
from src.bootstrap import app

"""Implement a way to select a cement."""
layout = html.Div([
    dcc.Dropdown(
        id='input-selected-report',
        options=[]
    ),
])


@app.callback(
    Output('input-selected-report', 'options'),
    Input('storage-report-file-loaded', 'data'),
)
def upload_selection_options(selected_file):
    files = glob.glob(STORAGE_DIRECTORY + '/*.csv')
    selector_options = [{'label': Path(file).name, 'value': Path(file).name} for file in files]
    return selector_options


@app.callback(
    Output('storage-selected-report', 'data'),
    [Input('input-selected-report', 'value')]
)
def store_selected_report(selected_report):
    if selected_report:
        return selected_report
