from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
import random
import json

with open('./assets/chartjs-chart-geo-test/nation.geojson', 'r') as f:
    geojson_nation_data = json.load(f)

nation = geojson_nation_data

with open('./assets/chartjs-chart-geo-test/states.geojson', 'r') as f:
    geojson_states_data = json.load(f)

states = geojson_states_data

chart = dbc.Col(
    [
        ChartJs(id='chart-5',type='choropleth',
            data = {
                'labels': [d['properties']['name'] for d in states],
                'datasets': [{
                    'label':'States',
                    'outline': nation,
                    'data': [{'feature': d, 'value': random.random() * 10} for d in states]
                }]
            },
            options = {
              'plugins': {
                'legend': {
                  'display': False
                },
                'datalabels': {
                  'display':False
                }
              },
              'scales': {
                'projection': {
                  'axis': 'x',
                  'projection': 'albersUsa'  
                },
                'color': {
                  'axis': 'x',
                  'quantize': 5,
                  'legend': {
                    'position': 'bottom-right',
                    'align': 'bottom'
                  },
                }
              },
            }
        )
    ],md=6
)