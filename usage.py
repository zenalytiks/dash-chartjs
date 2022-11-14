from dash_chartjs import ChartJs
import dash
from dash import html, Input, Output
import dash_bootstrap_components as dbc
import random

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])



app.layout = dbc.Container([
    html.H1('Dash ChartJs Component',className='text-center'),
    dbc.Button(id='gen-rand',children='Generate Random',n_clicks=0),
    
    dbc.Row(
      [
          dbc.Col(
              [
                  ChartJs(id='chart-1',type='line')
                
              ],md=6
          ),
          dbc.Col(
              [
                  ChartJs(id='chart-3',type='pie')
                  
              ],md=6
          )
      ]
    ),
    dbc.Row(
      [
          dbc.Col(
              [
                  ChartJs(id='chart-2',type='radar')
                  
              ],md=6
          ),
          dbc.Col(
              [
                  ChartJs(id='chart-4',type='bar')
                  
              ],md=6
          )
      ]
    )
    
])


@app.callback(
    [Output('chart-1','data'),Output('chart-1','options'),
    Output('chart-2','data'),Output('chart-2','options'),
    Output('chart-3','data'),Output('chart-3','options'),
    Output('chart-4','data'),Output('chart-4','options')
    ],
    Input('gen-rand','n_clicks')
)
def display_output(n):
    if n >= 0:
        columns = ['Jan','Feb','Mar','Apr','May','Jun','Jul']

        data1 = {
            'labels': columns,
            'datasets': [
                {
                    'label': 'Unfilled',
                    'fill': False,
                    'backgroundColor': 'rgba(53, 162, 235,0.2)',
                    'borderColor': 'rgba(53, 162, 235,1)',
                    'data': [random.randrange(-100,100,1) for i in range(7)]
                },
                {
                    'label': 'Dashed',
                    'fill': False,
                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'borderDash': [5, 5],
                    'data': [random.randrange(-100,100,1) for i in range(7)]
                },
                {
                    'label': 'Filled',
                    'fill': True,
                    'backgroundColor': 'rgba(255, 99, 132,1)',
                    'borderColor': 'rgba(255, 99, 132,0.2)',
                    'data': [random.randrange(-100,100,1) for i in range(7)]
                }
            ]
        } 

        options1 = {
            'responsive': True,
            'plugins': {
              'title': {
                'display': True,
                'text': 'Chart.js Line Chart'
              },
              'zoom':{
                'zoom':{
                  'wheel':{
                    'enabled': True
                  },
                  'mode':'xy'
                }
              }
            },
            'interaction': {
              'mode': 'index',
              'intersect': False
            },
            'scales': {
              'x': {
                'display': True,
                'title': {
                  'display': True,
                  'text': 'Month'
                }
              },
              'y': {
                'display': True,
                'title': {
                  'display': True,
                  'text': 'Value'
                }
              }
            }
        }

        data2 = {
            'labels': columns,
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

        }

        options2 = {
            'responsive': True,
            'plugins': {
              'title': {
                'display': True,
                'text': 'Chart.js Radar Chart'
              }
            }
        }

        data3 = {
            'labels': columns,
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
        }

        options3 = {
            'responsive': True,
            'plugins': {
              'legend': {
                'position': 'top',
              },
              'title': {
                'display': True,
                'text': 'Chart.js Pie Chart'
              }
            }
        }

        data4 = {
            'labels': columns,
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
        }

        options4 = {
            'responsive': True,
            'plugins': {
              'legend': {
                'position': 'top',
              },
              'zoom':{
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
              }
            }
        }

        

        return [data1, options1, data2, options2, data3, options3, data4, options4]
    


if __name__ == '__main__':
    app.run_server(debug=True)
