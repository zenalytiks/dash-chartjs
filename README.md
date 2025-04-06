# Dash Chartjs Component

Chart.js is one the most popular javascript charting library. 
Dash Chartjs Component is a Dash component library that renders [ChartJs React component](https://react-chartjs-2.js.org/) inside Dash App.

## Installation

```
pip install dash-chartjs
```

## Prop List
    
**id (str):** The ID used to identify this component in Dash callbacks.<br><br>
**type (str):** Chart.js chart type.<br><br>
**data (dict):** The data object that is passed into the Chart.js chart.<br><br>
**options (dict):** The options object that is passed into the Chart.js chart.<br><br>
**toolbox (boolean):** Toolbox with reset and download buttons for chart.<br><br>
**customJSFunctions (dict):** Write custom JS functions in dict format.<br><br>
**customPlugins (dict):** Write Plugins in dict format.<br><br>
**clickData (dict):** clickData returns the datasetIndex and index of data point clicked.<br><br>
**style (dict):** Defines CSS styles which will override styles previously set.<br><br>

## Additional Plugins Integrated
### [chartjs-plugin-zoom](https://www.chartjs.org/chartjs-plugin-zoom/latest/)
**Basic Configuration**<br>
```python
'options': {
    'plugins': {
      'zoom': {
        'zoom': {
          'wheel': {
            'enabled': True,
          },
          'pinch': {
            'enabled': True
          },
          'mode': 'xy',
        }
      }
    }
}
```
### [chartjs-plugin-datalabels](https://chartjs-plugin-datalabels.netlify.app/)
**Basic Configuration**<br>
```python
'options': {
  'plugins': {
    # Change options for ALL labels of THIS CHART
    'datalabels': {
      'color': '#36A2EB'
    }
  }
},
'data': {
  'datasets': [{
    # Change options only for labels of THIS DATASET
    'datalabels': {
      'color': '#FFCE56'
    }
  }]
}
```
**Example**
![datalables](https://github.com/zenalytiks/dash-chartjs/assets/31138706/f338eda9-4e0c-4128-ac72-972bbd488c6d)

### [chartjs-plugin-annotation](https://www.chartjs.org/chartjs-plugin-annotation/latest/)
**Basic Configuration**<br>
```python
'options': {
  'plugins': {
    'annotation': {
      'annotations': {
        'box1': {
          # Indicates the type of annotation
          'type': 'box',
          'xMin': 1,
          'xMax': 2,
          'yMin': 50,
          'yMax': 70,
          'backgroundColor': 'rgba(255, 99, 132, 0.25)'
        }
      }
    }
  }
}
```
**Example**
![annotations](https://github.com/zenalytiks/dash-chartjs/assets/31138706/1dec90df-69f9-4098-9b01-3f06d46248f1)

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


