#Basics Requirements
import pathlib
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px

#Dash Bootstrap Components
import dash_bootstrap_components as dbc

#data
import math
import numpy as np
import datetime as dt
import pandas as pd
import json
from sqlalchemy import create_engine

#Recall app
# from app import app

#callbacks
from callbacks import register_callbacks

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server
app.config['suppress_callback_exceptions']=True

###########################################################
#
#           APP LAYOUT:
#
###########################################################

#LOAD THE DIFFERENT FILES
from lib import title, sidebar, col_map, stats

#PLACE THE COMPONENTS IN THE LAYOUT
app.layout =html.Div(
    [
      col_map.map,
      stats.stats,
      # title.title,
      sidebar.sidebar,
    ],
    className="ds4a-app", #You can also add your own css files by locating them into the assets folder
)

register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
    # app.run_server(host='0.0.0.0',port=8080)