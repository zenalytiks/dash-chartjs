from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
import random

chart = dbc.Col(
    [
        ChartJs(id='chart-4',type='bar',
            data = {
                'labels': ['Jan','Feb','Mar','Apr','May','Jun','Jul'],
                'datasets': [
                  {
                    'label': 'Dataset 1',
                    'data': [random.randrange(-100,100,1) for i in range(7)],
                    'borderColor': 'rgba(75, 192, 192, 0.2)',
                    'backgroundColor': 'rgba(75, 192, 192, 1)',
                    'order': 1
                  },
                  {
                    'label': 'Dataset 2',
                    'data': [random.randrange(-100,100,1) for i in range(7)],
                    'borderColor': 'rgba(255, 99, 132, 1)',
                    'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                    'type': 'line',
                    'order': 0
                  }
                ]
            },
    
            options = {
                'responsive': True,
                'plugins': {
                  'legend': {
                    'position': 'top',
                  },
                  'tooltip': {
                      'callbacks': {
                          'footer': 'custom_footer'
                      }
                  },
                  'zoom':{
                    'pan': {
                      'enabled': True,
                      'mode': 'xy',
                    },
                    'zoom':{
                      'wheel':{
                        'enabled': True
                      },
                      'mode':'xy'
                    }
                  },
                  'title': {
                    'display': True,
                    'text': 'Chart.js Combined Line/Bar Chart'
                  },
                  'datalabels': {
                    'display':False
                  },
                }
            },
            customJSFunctions={
              'custom_footer':
              '''
              function (tooltipItems) {
                let sum = 0;
              
                tooltipItems.forEach(function(tooltipItem) {
                  sum += tooltipItem.parsed.y;
                });
                return 'Sum: ' + sum;
              }
              '''
              
            }
       )
        
    ],md=6
)