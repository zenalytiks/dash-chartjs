from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc
import random

chart = dbc.Col(
    [
        ChartJs(id='chart-1',type='line',
        data = {
            'labels': ['Jan','Feb','Mar','Apr','May','Jun','Jul'],
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
        },

        options = {
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
        },
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
)
        