from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
import requests


url_pcp = 'https://raw.githubusercontent.com/derhuerst/mtcars/master/index.json'
response_pcp = requests.get(url_pcp)
pcp_sample_data = response_pcp.json()
attrs = ['mpg', 'hp', 'wt', 'qsec', 'gear', 'drat', 'disp', 'cyl']

chart = dbc.Col(
    [
        ChartJs(id='chart-7',type='pcp',
            data = {
                'labels': [c['model'] for c in pcp_sample_data],
                'datasets': [
                     {
                         'label': attr,
                         'data': [car[attr] for car in pcp_sample_data],
                         'backgroundColor': 'none'
                     }
                     for attr in attrs
                 ]
            },
            options = {
                'plugins': {
                  'datalabels': {
                    'display':False
                  }
                }
            })
    ],md=6
)