from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
import random


def random_values(count, min_val, max_val):
    return [random.uniform(min_val, max_val) for _ in range(count)]

chart = dbc.Col(
    [
        ChartJs(id='chart-9',type='boxplot',
            data = {
                # define label tree
                'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                'datasets': [
                    {
                        'label': 'Dataset 1',
                        'backgroundColor': 'rgba(255,0,0,0.5)',
                        'borderColor': 'red',
                        'borderWidth': 1,
                        'outlierColor': '#999999',
                        'padding': 10,
                        'itemRadius': 0,
                        'data': [
                            random_values(100, 0, 100),
                            random_values(100, 0, 20),
                            random_values(100, 20, 70),
                            random_values(100, 60, 100),
                            random_values(40, 50, 100),
                            random_values(100, 60, 120),
                            random_values(100, 80, 100),
                        ]
                    },
                    {
                        'label': 'Dataset 2',
                        'backgroundColor': 'rgba(0,0,255,0.5)',
                        'borderColor': 'blue',
                        'borderWidth': 1,
                        'outlierColor': '#999999',
                        'padding': 10,
                        'itemRadius': 0,
                        'data': [
                            random_values(100, 60, 100),
                            random_values(100, 0, 100),
                            random_values(100, 0, 20),
                            random_values(100, 20, 70),
                            random_values(40, 60, 120),
                            random_values(100, 20, 100),
                            random_values(100, 80, 100),
                        ]
                    }
                ]
            },
            options= {
              'responsive': True,
              'legend': {
                'position': 'top',
              },
              'title': {
                'display': True,
                'text': 'Chart.js Box Plot Chart'
              },
              'plugins': {
                  'datalabels': {
                    'display':False
                  }
              }
            }
        )
    ],md=6
)