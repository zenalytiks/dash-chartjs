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

- customJSFunctions (dict; optional):
    Write custom JS functions in dict format.

- customPlugins (dict; optional):
    Write Plugins in dict format.

- data (dict; default {    datasets: []}):
    The data object that is passed into the Chart.js chart.

- options (dict; optional):
    The options object that is passed into the Chart.js chart.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- toolbox (boolean; default True):
    Toolbox with reset and download buttons for chart.

- type (string; optional):
    Chart.js chart type."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_chartjs'
    _type = 'ChartJs'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, type=Component.UNDEFINED, data=Component.UNDEFINED, options=Component.UNDEFINED, toolbox=Component.UNDEFINED, clickData=Component.UNDEFINED, customJSFunctions=Component.UNDEFINED, customPlugins=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'clickData', 'customJSFunctions', 'customPlugins', 'data', 'options', 'style', 'toolbox', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clickData', 'customJSFunctions', 'customPlugins', 'data', 'options', 'style', 'toolbox', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ChartJs, self).__init__(**args)
