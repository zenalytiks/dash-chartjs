from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
import random

chart = dbc.Col(
    [
        ChartJs(id='chart-2',type='radar',
          data = {
              'labels': ['Jan','Feb','Mar','Apr','May','Jun','Jul'],
              'datasets': [
                  {
                      'label': 'Dataset 1',
                      'data': [random.randrange(-100,100,1) for i in range(7)],
                      'borderColor': 'rgba(153, 102, 255, 1)',
                      'backgroundColor': 'rgba(153, 102, 255, 0.2)',
                  },
                  {
                      'label': 'Dataset 2',
                      'data': [random.randrange(-100,100,1) for i in range(7)],
                      'borderColor': 'rgba(255, 206, 86, 1)',
                      'backgroundColor': 'rgba(255, 206, 86, 0.2)',
                  }
              ]

          },

          options = {
              'responsive': True,
              'plugins': {
                'title': {
                  'display': True,
                  'text': 'Chart.js Radar Chart'
                },
                'datalabels': {
                  'display':False
                }
              }
          })
                    
    ],md=6
)