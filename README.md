## Cement analysis with Dash

During the implementation major part of time was spend on learning dash plot, and reading about types of correlations between and the compressive strength and quantities. 

- I was reading what is [google: "what is corelation in cement concrete" https://bit.ly/2J6Qv29][https://bit.ly/2J6Qv29]
- but the answer was [https://bit.ly/3mvIoKS][https://bit.ly/3mvIoKS]

just was needed to use another type of the graph (linear -> markers) to get in meaningful

### How to launch

There are two ways how to launch application

#### 1. Manual

run the command `python main.py`

Note: please be sure that you have installed all dependencies `python -m pip install -r requirements.txt`

Note 2: To keep work environment (workstation) clean, please use local env `python -m venv env` and please use in command below the python instance from local environment (Windows)`env\Script\python.exe` or (Linux) `env\bin\python`

To stop the app needs to terminate process or close console


#### 2. Dockerized

If you have a docker installed on your machine, it's much easier to launch the application `docker-compose up`,

now application accessed on [http://localhost]

To stop the aplication run the command `docker-compose down`

### Implementation description

- Created a dashboard app with **Dash**.
with routing by url supporting

- Read data from the CSV files (one file per cement, `quantities.md` describes their contents).

application provide functionality to select csv source files from existing on server, or upload new 

- Implement a way to select a cement.

selection of the cement provided via selection csv source files

- Implement a detail view that shows one cement with a graphical representation containing all strength data (2, 7 and 28 day).

used dash_component_core.Graph

- In the same detail view, make a table with the strength and laboratory data.

used dash_table.DataTable, provided functionality to choose the columns in the table.

- Visualize the correlation between a quantity and the compressive strength. The quantity should be selectable.

used dash_component_core.Graph
