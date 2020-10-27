# - Create a dashboard app with **Dash**.
# - Read data from the CSV files (one file per cement, `quantities.md` describes their contents).
# - Implement a way to select a cement.
# - Implement a detail view that shows one cement with a graphical representation containing all strength data (2, 7 and 28 day).
# - In the same detail view, make a table with the strength and laboratory data.
# - Visualize the correlation between a quantity and the compressive strength. The quantity should be selectable.
import os

from config.config import APPLICATION_MODE_DEBUGABLE
from src.bootstrap import app
from src.route import route


if __name__ == '__main__':
    route(app)
    app.run_server(debug=APPLICATION_MODE_DEBUGABLE)
