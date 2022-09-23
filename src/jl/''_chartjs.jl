# AUTO GENERATED FILE - DO NOT EDIT

export ''_chartjs

"""
    ''_chartjs(;kwargs...)

A ChartJs component.
This component renders ChartJs React component inside Dash App.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `data` (Dict; optional): The data object that is passed into the Chart.js chart
- `options` (Dict; optional): The options object that is passed into the Chart.js chart
- `type` (String; optional): Chart.js chart type
"""
function ''_chartjs(; kwargs...)
        available_props = Symbol[:id, :data, :options, :type]
        wild_props = Symbol[]
        return Component("''_chartjs", "ChartJs", "dash_chartjs", available_props, wild_props; kwargs...)
end

