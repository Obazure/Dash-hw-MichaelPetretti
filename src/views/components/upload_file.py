from datetime import datetime
import os
import dash_core_components as dcc
import dash_html_components as html
import base64
from dash.dependencies import Input, Output, State
from config.config import STORAGE_DIRECTORY
from src.assets.styles import file_uploader_style
from src.bootstrap import app

layout = html.Div([
    dcc.Upload(
        id='upload-file',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select new csv report')
        ]),
        style=file_uploader_style,
        # Allow multiple files to be uploaded
        multiple=False
    ),
    html.P('Note: loading a new file with an existing name may overwrite the existing file on the server.'),
    html.P(id='output-data-upload'),
])


@app.callback(
    [Output('output-data-upload', 'children'),
     Output('storage-report-file-loaded', 'data')],
    [Input('upload-file', 'contents'),
     Input('upload-file', 'filename')]
)
def upload_file(contents, filename):
    if contents is not None:
        save_file(contents, filename)
        return str(filename) + ' uploaded.', str(filename) + str(datetime.now())
    return '', ''


def save_file(content, filename):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(STORAGE_DIRECTORY, filename), "wb") as fp:
        fp.write(base64.decodebytes(data))
