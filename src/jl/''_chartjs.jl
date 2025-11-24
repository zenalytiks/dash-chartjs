# AUTO GENERATED FILE - DO NOT EDIT

export ''_chartjs

"""
    ''_chartjs(;kwargs...)

A ChartJs component.
This component renders ChartJs React component inside Dash App.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `actions` (optional): List of action objects with name and handler properties.
Each action will be rendered as a button below the chart.. actions has the following type: Array of lists containing elements 'name', 'handler'.
Those elements have the following types:
  - `name` (String; required)
  - `handler` (String; required)s
- `clickData` (Dict; optional): clickData returns the datasetIndex and index of data point clicked.
- `customJSFunctions` (Dict; optional): Write custom JS functions in dict format.
- `customPlugins` (Dict; optional): Write Plugins in dict format.
- `data` (Dict; optional): The data object that is passed into the Chart.js chart.
- `options` (Dict; optional): The options object that is passed into the Chart.js chart.
- `redraw` (Bool; optional): Teardown and redraw chart on every update.
- `style` (Dict; optional): Defines CSS styles which will override styles previously set.
- `toolbox` (Bool; optional): Toolbox with reset and download buttons for chart.
- `type` (String; optional): Chart.js chart type.
"""
function ''_chartjs(; kwargs...)
        available_props = Symbol[:id, :actions, :clickData, :customJSFunctions, :customPlugins, :data, :options, :redraw, :style, :toolbox, :type]
        wild_props = Symbol[]
        return Component("''_chartjs", "ChartJs", "dash_chartjs", available_props, wild_props; kwargs...)
end

