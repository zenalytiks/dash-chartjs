from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc

chart = dbc.Col(
    [
        ChartJs(id='chart-8',type='matrix',
            data = {
                'datasets': [{
                  'label': 'My Matrix',
                  'data': [
                    {'x': 1, 'y': 1, 'v': 11},
                    {'x': 1, 'y': 2, 'v': 12},
                    {'x': 1, 'y': 3, 'v': 13},
                    {'x': 2, 'y': 1, 'v': 21},
                    {'x': 2, 'y': 2, 'v': 22},
                    {'x': 2, 'y': 3, 'v': 23},
                    {'x': 3, 'y': 1, 'v': 31},
                    {'x': 3, 'y': 2, 'v': 32},
                    {'x': 3, 'y': 3, 'v': 33}
                  ],
                  'backgroundColor': 'custom_background_color',
                  'borderColor': 'custom_border_color',
                  'borderWidth': 1,
                  'width': 'custom_width',
                  'height': 'custom_height'
                }]
            },
            
            options = {
                'plugins': {
                  'legend': False,
                  'tooltip': {
                    'callbacks': {
                      'title': 'custom_title',
                      'label': 'custom_label'
                    }
                  },
                  'datalabels': {
                    'display':False
                  }
                },
                'scales': {
                  'x': {
                    'ticks': {
                      'stepSize': 1
                    },
                    'grid': {
                      'display': False
                    }
                  },
                  'y': {
                    'offset': True,
                    'ticks': {
                      'stepSize': 1
                    },
                    'grid': {
                      'display': False
                    }
                  }
                }
            },
            customJSFunctions = {
                'custom_background_color':
                '''
                function (context) {
                    const value = context.dataset.data[context.dataIndex].v;
                    const alpha = (value - 5) / 40;
                    const clampedAlpha = Math.max(0, Math.min(1, alpha)); // clamp alpha between 0 and 1
                    return `rgba(0, 128, 0, ${clampedAlpha.toFixed(2)})`;
                }
                ''',
                'custom_border_color':
                '''
                function (context) {
                    const value = context.dataset.data[context.dataIndex].v;
                    const alpha = (value - 5) / 40;
                    const clampedAlpha = Math.max(0, Math.min(1, alpha)); // Clamp alpha between 0 and 1
                    return `rgba(0, 100, 0, ${clampedAlpha.toFixed(2)})`;
                }
                ''',
                'custom_title':
                '''
                  function () {
                    return '';
                  }
                ''',
                'custom_label':
                '''
                  function (context) {
                    const v = context.dataset.data[context.dataIndex];
                    return ['x: ' + v.x, 'y: ' + v.y, 'v: ' + v.v];
                  }
                ''',
                'custom_width':
                '''
                function (context) {
                  var chartArea = context.chart && context.chart.chartArea;
                  if (!chartArea) return 0;
                  return chartArea.width / 3 - 1;
                }
                ''',
                'custom_height':
                '''
                function (context) {
                  var chartArea = context.chart && context.chart.chartArea;
                  if (!chartArea) return 0;
                  return chartArea.height / 3 - 1;
                }
                '''
            }
        )
    ],md=6
)