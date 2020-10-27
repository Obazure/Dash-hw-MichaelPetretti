import os
from pathlib import Path

import dash

from config.config import STORAGE_DIRECTORY
from src.views import error_page
from src.views.components.upload_file import save_file


def test_bsly001_simple_component(dash_duo):
    app = dash.Dash(__name__)
    app.layout = error_page.layout
    dash_duo.start_server(app)
    dash_duo.wait_for_text_to_equal("#error-message", "Error 404, no content to present", timeout=4)
    assert dash_duo.find_element("#error-message").text == "0"
    assert dash_duo.get_logs() == [], "browser console should contain no error"


def test_bsly002_file_saves(dash_duo):
    content = 'test_content'
    filename = 'new.csv'

    save_file(content, filename)

    filepath = os.path.join(STORAGE_DIRECTORY, filename)
    file = Path(filepath)
    assert file.is_file()
