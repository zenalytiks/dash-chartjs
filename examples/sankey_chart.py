from dash_chartjs import ChartJs
import dash_bootstrap_components as dbc

chart = dbc.Col(
    [
        ChartJs(id='chart-11',type='sankey',
            data = {
                'datasets': [
                  {
                    'data': [
                      { 'from': "Oil", 'to': "Fossil Fuels", 'flow': 15 },
                      { 'from': "Natural Gas", 'to': "Fossil Fuels", 'flow': 20 },
                      { 'from': "Coal", 'to': "Fossil Fuels", 'flow': 25 },
                      { 'from': "Coal", 'to': "Electricity", 'flow': 25 },
                      { 'from': "Fossil Fuels", 'to': "Energy", 'flow': 60 },
                      { 'from': "Electricity", 'to': "Energy", 'flow': 25 }
                    ],
                    'priority': {
                      'Oil': 1,
                      'Narural Gas': 2,
                      'Coal': 3,
                      'Fossil Fuels': 1,
                      'Electricity': 2,
                      'Energy': 1
                    },
                    'labels':{
                      'Oil': 'black gold (label changed)'
                    },
                    'colorFrom': 'red',
                    'colorTo': 'green',
                    'borderWidth': 2,
                    'borderColor': 'black'
                  }
                ]
            },
            options = {
                'plugins': {
                    'datalabels': {
                        'display': False
                    }
                }
            }
        )
    ],md=6
)