from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
import requests

url_graph = 'https://raw.githubusercontent.com/sgratzl/chartjs-chart-graph/main/docs/examples/miserables.json'
response_graph = requests.get(url_graph)
graph_sample_data = response_graph.json()

chart = dbc.Col(
    [
        ChartJs(id='chart-6',type='forceDirectedGraph',
            data = {
              'labels': [d['id'] for d in graph_sample_data['nodes']],
              'datasets': [{
                'pointBackgroundColor': 'steelblue',
                'pointRadius': 5,
                'data': graph_sample_data['nodes'],
                'edges': graph_sample_data['links']
              }]
            },
            options = {
              'legend': {
                'display': False
              },
              'plugins': {
                'datalabels': {
                  'display':False
                }
              }
              
            },
            redraw=True
        )
    ],md=12
)