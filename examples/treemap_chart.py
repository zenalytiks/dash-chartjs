from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc

chart = dbc.Col(
    [
        ChartJs(id='chart-10',type='treemap',
            data = {
                'datasets': [
                  {
                    'label': 'My treemap dataset',
                    'tree': [15, 6, 6, 5, 4, 3, 2, 2],
                    'borderColor': 'green',
                    'borderWidth': 1,
                    'spacing': 0,
                    'backgroundColor': 'color_from_raw',
                  }
                ]
            },
            options = {
              'plugins': {
                'title': {
                  'display': True,
                  'text': 'My treemap chart'
                },
                'legend': {
                  'display': False
                },
                'datalabels': {
                    'display': False
                }
              }
            },
            customJSFunctions = {
                'color_from_raw':
                '''
                function colorFromRaw(ctx) {
                  if (ctx.type !== 'data') {
                    return 'transparent';
                  }
                  const value = ctx.raw.v;
                  let alpha = (1 + Math.log(value)) / 5;
                  alpha = Math.max(0, Math.min(1, alpha)); // Clamp alpha to [0, 1]
                  
                  // 'green' RGB = (0, 128, 0)
                  return `rgba(0, 128, 0, ${alpha.toFixed(2)})`;
                }
                '''
            }
        )
    ],md=6
)
        