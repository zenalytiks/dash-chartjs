# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args

ComponentType = typing.Union[
    str,
    int,
    float,
    Component,
    None,
    typing.Sequence[typing.Union[str, int, float, Component, None]],
]

NumberType = typing.Union[
    typing.SupportsFloat, typing.SupportsInt, typing.SupportsComplex
]


class ChartJs(Component):
    """A ChartJs component.
This component renders ChartJs React component inside Dash App.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- actions (list of dicts; optional):
    List of action objects with name and handler properties.  Each
    action will be rendered as a button below the chart.

    `actions` is a list of dicts with keys:

    - name (string; required)

    - handler (string; required)

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

- redraw (boolean; default False):
    Teardown and redraw chart on every update.

- toolbox (boolean; default True):
    Toolbox with reset and download buttons for chart.

- type (string; optional):
    Chart.js chart type."""
    _children_props: typing.List[str] = []
    _base_nodes = ['children']
    _namespace = 'dash_chartjs'
    _type = 'ChartJs'
    Actions = TypedDict(
        "Actions",
            {
            "name": str,
            "handler": str
        }
    )


    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        type: typing.Optional[str] = None,
        data: typing.Optional[dict] = None,
        options: typing.Optional[dict] = None,
        redraw: typing.Optional[bool] = None,
        toolbox: typing.Optional[bool] = None,
        clickData: typing.Optional[dict] = None,
        customJSFunctions: typing.Optional[dict] = None,
        customPlugins: typing.Optional[dict] = None,
        actions: typing.Optional[typing.Sequence["Actions"]] = None,
        style: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'actions', 'clickData', 'customJSFunctions', 'customPlugins', 'data', 'options', 'redraw', 'style', 'toolbox', 'type']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'actions', 'clickData', 'customJSFunctions', 'customPlugins', 'data', 'options', 'redraw', 'style', 'toolbox', 'type']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(ChartJs, self).__init__(**args)

setattr(ChartJs, "__init__", _explicitize_args(ChartJs.__init__))
