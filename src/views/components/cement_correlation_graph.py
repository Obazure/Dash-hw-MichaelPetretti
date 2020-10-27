from collections import defaultdict

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from src.bootstrap import app

"""Visualize the correlation between a quantity and the compressive strength. The quantity should be selectable."""
layout = html.Div([
    html.Div(className='mt-5 mb-5', children=[
        dcc.Graph(id='cement-correlation-graph'),
        html.Label('Choose quantity'),
        dcc.Dropdown(id='cement-quantity'),
    ]),
])


@app.callback([Output('cement-quantity', 'options'),
               Output('cement-quantity', 'value')],
              Input('storage-chart-data', 'data'))
def init_quantity_selector(data):
    common_columns = [
        'recorded-at',
        'sample-id',
        'd10',
        'd50',
        "d'",
        'd84',
        'd90',
        'd95',
    ]
    xrf_lab_columns = [
        'CO2',
        'limestone content',
        'CaO',
        'MgO',
        'Al2O3',
        'SO3',
        'K2O',
        'Na2O',
        'Cl-',
        'TiO2',
        'MnO',
        'S',
        'HS',
        'HS-XRF-sulfate-free',
        'Na2O-equiv.',
    ]
    xrc_lab_columns = [
        'C3S',
        'C2S',
        'C3A-orthorhombic',
        'C3A-cubic',
        'C4AF',
        'unslaked lime',
        'calcite',
        'HS-XRC'
    ]
    other_lab_columns = [
        'reflectance L',
        'reflectance a',
        'reflectance b',
        'water-demand',
        'solidify-start',
        'solidify-end',
        'Le Chatelier'
    ]
    options = [{'label': x.title(), 'value': x} for x in common_columns]
    options += [{'label': 'XRF: ' + x, 'value': x} for x in xrf_lab_columns]
    options += [{'label': 'XRC: ' + x, 'value': x} for x in xrc_lab_columns]
    options += [{'label': x.title(), 'value': x} for x in other_lab_columns]
    value = "d'"
    return options, value


@app.callback(Output('cement-correlation-graph', 'figure'),
              [Input('storage-chart-data', 'data'),
               Input('cement-quantity', 'value')])
def on_data_set_correlation_graph(data, quantity):
    figure = {
        'layout': {
            'title': 'Correlation between a quantity and the compressive strength'
        }
    }
    if data:
        aggregation = defaultdict(lambda: defaultdict(list))
        for row in data:
            for field in ['comp. str. 2d', 'comp. str. 7d', 'comp. str. 28d']:
                if field in row:
                    a = aggregation[field]
                    a['name'] = field.title()
                    a['mode'] = 'markers'
                    a['x'].append(row[quantity])
                    a['y'].append(row[field])
        figure['data'] = [x for x in aggregation.values()]
        return figure
    return figure
