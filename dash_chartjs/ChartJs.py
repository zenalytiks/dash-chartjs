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

- data (dict; default {    datasets: []}):
    The data object that is passed into the Chart.js chart.

- options (dict; optional):
    The options object that is passed into the Chart.js chart.

- style (dict; optional):
    Defines CSS styles which will override styles previously set.

- type (string; optional):
    Chart.js chart type."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_chartjs'
    _type = 'ChartJs'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, type=Component.UNDEFINED, data=Component.UNDEFINED, options=Component.UNDEFINED, clickData=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'clickData', 'data', 'options', 'style', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clickData', 'data', 'options', 'style', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ChartJs, self).__init__(**args)
