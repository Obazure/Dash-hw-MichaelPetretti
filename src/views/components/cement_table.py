import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State

from src.bootstrap import app

"""In the same detail view, make a table with the strength and laboratory data."""
layout = html.Div([
    html.H5('Table with the strength and laboratory data', className='text-center'),
    html.Div(className='mt-3 mb-3', children=[
        html.Label('Table columns'),
        dcc.Dropdown(id='cement-table-columns', multi=True),
    ]),
    html.Div(className='mt-3 mb-3', children=[
        html.Label('Table data'),
        dash_table.DataTable(id='cement-table'),
    ])
])


@app.callback(
    [Output('cement-table-columns', 'options'),
     Output('cement-table-columns', 'value')],
    Input('storage-chart-data', 'data'))
def set_cement_table_columns(data):
    common_columns = [
        'recorded-at',
        'sample-id',
        'comp. str. 2d',
        'comp. str. 7d',
        'comp. str. 28d',
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

    value = ['recorded-at', 'comp. str. 7d', 'comp. str. 2d', 'comp. str. 28d', 'CO2', 'SO3', 'Cl-', 'TiO2',
             'C3S', 'HS-XRC']
    return options, value


@app.callback(Output('cement-table', 'columns'),
              Input('cement-table-columns', 'value'))
def update_table_columns(columns):
    return [{"name": i, "id": i} for i in columns]


@app.callback(Output('cement-table', 'data'),
              Input('storage-chart-data', 'data'),
              State('cement-table-columns', 'value'))
def on_data_set_table(data, columns):
    if data:
        return data
    return []
