# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ChartJs(Component):
    """A ChartJs component.
This component renders ChartJs React component inside Dash App.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- clickData (dict; optional):
    clickData returns the datasetIndex and index of data point
    clicked.

- customCanvasBackgroundColor (string; optional):
    Set the Background color of Canvas.

- data (dict; default {    datasets: []}):
    The data object that is passed into the Chart.js chart.

- linearGradientDirection (a value equal to: 'vertical', 'horizontal'; default 'vertical'):
    Set the direction of Linear Gradient. Either 'horizontal' or
    'vertical'. Vertical is default.

- linearGradientList (list; optional):
    List of colors for the Linear Gradient.

- options (dict; optional):
    The options object that is passed into the Chart.js chart.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- toolbox (boolean; default True):
    Toolbox with reset and download buttons for chart.

- type (string; optional):
    Chart.js chart type.

- useGradient (a value equal to: 'borderColor', 'backgroundColor', 'both'; default 'both'):
    Apply Linear Gradient on 'borderColor', 'backgroundColor' or on
    'both'. Applies on both by default."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_chartjs'
    _type = 'ChartJs'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, type=Component.UNDEFINED, data=Component.UNDEFINED, options=Component.UNDEFINED, toolbox=Component.UNDEFINED, linearGradientList=Component.UNDEFINED, linearGradientDirection=Component.UNDEFINED, useGradient=Component.UNDEFINED, customCanvasBackgroundColor=Component.UNDEFINED, clickData=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'clickData', 'customCanvasBackgroundColor', 'data', 'linearGradientDirection', 'linearGradientList', 'options', 'style', 'toolbox', 'type', 'useGradient']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clickData', 'customCanvasBackgroundColor', 'data', 'linearGradientDirection', 'linearGradientList', 'options', 'style', 'toolbox', 'type', 'useGradient']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ChartJs, self).__init__(**args)
