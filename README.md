# Dash Chartjs Component

Chart.js is one the most popular javascript charting library. 
Dash Chartjs Component is a Dash component library that renders [ChartJs React component](https://react-chartjs-2.js.org/) inside Dash App.

## Installation

```
pip install dash-chartjs
```

## Prop List
    
**id:** The ID used to identify this component in Dash callbacks.<br>
**type:** Chart.js chart type.<br>
**data:** The data object that is passed into the Chart.js chart.<br>
**options:** The options object that is passed into the Chart.js chart.<br>
**toolbox:** Toolbox with reset and download buttons for chart.<br>
**linearGradientList:** List of colors for the Linear Gradient.<br>
**linearGradientDirection:** Set the direction of Linear Gradient. Either 'horizontal' or 'vertical'. Vertical is default.<br>
**useGradient:** Apply Linear Gradient on 'borderColor', 'backgroundColor' or on 'both'. Applies on both by default.<br>
**clickData:** clickData returns the datasetIndex and index of data point clicked.<br>
**style:** Defines CSS styles which will override styles previously set.<br>

## Basic Usage

```python
from dash import dash,html
import pandas as pd
from dash_chartjs import ChartJs

app = dash.Dash(__name__,meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])

df = pd.read_csv('https://raw.githubusercontent.com/JetBlack101/visitors-to-georgia-ts-analysis/main/Data/VisitorsToGeorgia_2011-2019.csv')

df['Date'] = pd.to_datetime(df['Date'])

x = df['Date']
y = df['Visitors']

data = {
    'labels': x,
    'datasets': [{
        'label': 'Visitors to Georgia',
        'data': y,
        'fill':'false',
        'borderColor': 'rgb(75, 192, 192)',
        'tension': 0.1
    }]
}
options = {
    'scales': {
        'x': {
            'type':'time'
        }
    },
    'plugins':{
        'zoom':{
            'zoom':{
                'wheel':{
                    'enabled': True
                },
            'mode':'xy'
            }
        }
    } 
}


app.layout = html.Div(
    [
        ChartJs(type='line',data=data,options=options)
    ]
)

if __name__ == '__main__':
    app.run_server(debug=False)
```

## Demo


https://user-images.githubusercontent.com/31138706/192035295-0a10eb80-0881-443b-8ea8-7dfd98eb77f3.mp4


