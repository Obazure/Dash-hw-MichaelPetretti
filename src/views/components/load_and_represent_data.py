import os
from pathlib import Path

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from config.config import STORAGE_DIRECTORY
from src.bootstrap import app
import pandas as pd

from src.views.components import cement_graph, cement_table, cement_correlation_graph

layout = html.Div([
    dcc.Store(id='storage-chart-data', storage_type='session'),
    html.Div(id='report-content'),
])


@app.callback(Output('report-content', 'children'),
              Input('storage-selected-report', 'data'))
def init_view(data):
    if data:
        return html.Div([
            cement_graph.layout,
            cement_table.layout,
            cement_correlation_graph.layout
        ])
    return html.P('Choose report to see the report content.')


@app.callback(Output('storage-chart-data', 'data'),
              Input('report-content', 'children'),
              State('storage-selected-report', 'data'))
def read_report_file(trigger, filename):
    """Read data from the CSV files (one file per cement, quantities.md describes their contents)."""
    if filename:
        filepath = os.path.join(STORAGE_DIRECTORY, filename)
        file = Path(filepath)
        if file.is_file():
            df = pd.read_csv(filepath)
            df = df.rename(columns=lambda x: x.strip())
            return df.to_dict('records')
