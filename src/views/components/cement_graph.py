from collections import defaultdict

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.bootstrap import app

"""Implement a detail view that shows one cement with a graphical representation containing all strength data (2, 
7 and 28 day). """
layout = html.Div(className='mt-5 mb-5', children=[
    dcc.Graph(id='cement-graph'),
])


@app.callback(Output('cement-graph', 'figure'),
              [Input('storage-chart-data', 'data')])
def on_data_set_cement_strength_graph(data):
    figure = {
        'layout': {
            'title': 'Cement strength chart (2d, 7d, 28d)'
        }
    }
    if data:
        aggregation = defaultdict(lambda: defaultdict(list))
        for row in data:
            for field in ['comp. str. 2d', 'comp. str. 7d', 'comp. str. 28d']:
                if field in row:
                    a = aggregation[field]
                    a['name'] = field.title()
                    a['mode'] = 'lines'
                    a['x'].append(row['recorded-at'])
                    a['y'].append(row[field])
        figure['data'] = [x for x in aggregation.values()]
        return figure
    return figure
