from dash_chartjs import ChartJs
from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc
import random
import json

with open('./assets/chartjs-chart-geo-test/nation.geojson', 'r') as f:
    geojson_nation_data = json.load(f)

nation = geojson_nation_data

with open('./assets/chartjs-chart-geo-test/states.geojson', 'r') as f:
    geojson_states_data = json.load(f)

states = geojson_states_data

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])



app.layout = dbc.Container([
    html.H1('Dash ChartJs Component',className='text-center'),
    dbc.Button(id='gen-rand',children='Generate Random',n_clicks=0),
    
    dbc.Row(
      [
          dbc.Col(
              [
                  ChartJs(id='chart-1',type='line',
                  customJSFunctions={
                      'yaxis_formatter':
                      '''
                      function (value, index, ticks) {
                          return '$' + value;
                      }
                      ''',
                      'custom_gradient': 
                      '''
                      function (ctx) {
                          const canvas = ctx.chart.ctx;
                          const gradient = canvas.createLinearGradient(0, 25, 0, 300);
                          gradient.addColorStop(0, "rgba(149, 76, 233, 0.5)");
                          gradient.addColorStop(0.35, "rgba(149, 76, 233, 0.25)");
                          gradient.addColorStop(1, "rgba(149, 76, 233, 0)");
                  
                          return gradient;
                      }
                      '''
                  },
                  customPlugins={
                      'myCustomPlugin':
                      '''
                      {
                         id: 'myCustomPlugin',
                         beforeDraw: (chart, args, options) => {
                           const { ctx } = chart;
                           ctx.save();
                           ctx.globalCompositeOperation = 'destination-over';
                           ctx.fillStyle = options.color || '#000';
                           ctx.fillRect(0, 0, chart.width, chart.height);
                           ctx.restore();
                         },
                      }
                      '''
                  }
                  )
                
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
                  ChartJs(id='chart-4',type='bar',customJSFunctions={
                      'custom_footer':
                      '''
                      function (tooltipItems) {
                        let sum = 0;
                      
                        tooltipItems.forEach(function(tooltipItem) {
                          sum += tooltipItem.parsed.y;
                        });
                        return 'Sum: ' + sum;
                      }
                      ''',
                      
                  },
                 )
                  
              ],md=6
          ),
          dbc.Col(
              [
                  ChartJs(id='chart-5',type='choropleth')
              ]
          )
      ]
    )
    
])


@app.callback(
    [Output('chart-1','data'),Output('chart-1','options'),
    Output('chart-2','data'),Output('chart-2','options'),
    Output('chart-3','data'),Output('chart-3','options'),
    Output('chart-4','data'),Output('chart-4','options'),
    Output('chart-5','data'),Output('chart-5','options')
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
                    'fill': True,
                    'borderWidth': 2,
                    'backgroundColor': 'custom_gradient',
                    'pointBackgroundColor': "rgba(149, 76, 233, 1)",
                    'borderColor': "rgba(149, 76, 233, 1)",
                    'pointStyle': 'triangle',
                    'pointRadius': 6,
                    'data': [random.randrange(0,100,1) for i in range(7)]
                },
                {
                    'label': 'Dashed',
                    'fill': False,
                    'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                    'borderColor': 'rgba(75, 192, 192, 1)',
                    'borderDash': [5, 5],
                    'pointStyle': 'star',
                    'pointRadius': 6,
                    'data': [random.randrange(-100,100,1) for i in range(7)]
                },
                {
                    'label': 'Filled',
                    'fill': True,
                    'backgroundColor': 'rgba(255, 99, 132,1)',
                    'borderColor': 'rgba(255, 99, 132,0.2)',
                    'pointStyle': 'circle',
                    'pointRadius': 6,
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
              'tooltip': {
                  'usePointStyle': True
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
              'datalabels': {
                'display':False
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
                },
                'ticks': {
                    'major': {
                        'enabled': True
                    },
                    'display': True,
                    'autoSkip': False,
                    'callback': 'yaxis_formatter'
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
              },
              'datalabels': {
                'display':False
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
              },
              'datalabels': {
                'display':False
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
        }

        

        data5={
            'labels': [d['properties']['name'] for d in states],
            'datasets': [{
                'label':'States',
                'outline': nation,
                'data': [{'feature': d, 'value': random.random() * 10} for d in states]
            }]
        }
        options5={
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

        

        return [data1, options1, data2, options2, data3, options3, data4, options4, data5, options5]
    


if __name__ == '__main__':
    app.run(debug=True)
