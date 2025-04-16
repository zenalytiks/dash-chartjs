from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
import random

chart = dbc.Col(
    [
        ChartJs(id='chart-3',type='pie',
          data = {
              'labels': ['Jan','Feb','Mar','Apr','May','Jun','Jul'],
              'datasets': [
                {
                  'label': 'Dataset 1',
                  'data': [random.randrange(-100,100,1) for i in range(6)],
                  'backgroundColor': [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                  ],
                  'borderColor': [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                  ],
                  'borderWidth': 1
                }
              ]
          },

          options = {
              'responsive': True,
              'plugins': {
                'legend': {
                  'position': 'top',
                },
                'title': {
                  'display': True,
                  'text': 'Chart.js Pie Chart'
                },
                'datalabels': {
                  'display':False
                }
              }
          })
        
    ],md=6
)