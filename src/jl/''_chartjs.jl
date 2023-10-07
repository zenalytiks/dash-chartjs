# AUTO GENERATED FILE - DO NOT EDIT

export ''_chartjs

"""
    ''_chartjs(;kwargs...)

A ChartJs component.
This component renders ChartJs React component inside Dash App.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `clickData` (Dict; optional): clickData returns the datasetIndex and index of data point clicked.
- `customCanvasBackgroundColor` (String; optional): Set the Background color of Canvas.
- `data` (Dict; optional): The data object that is passed into the Chart.js chart.
- `linearGradientDirection` (a value equal to: 'vertical', 'horizontal'; optional): Set the direction of Linear Gradient. Either 'horizontal' or 'vertical'. Vertical is default.
- `linearGradientList` (Array; optional): List of colors for the Linear Gradient.
- `options` (Dict; optional): The options object that is passed into the Chart.js chart.
- `style` (Dict; optional): Defines CSS styles which will override styles previously set.
- `toolbox` (Bool; optional): Toolbox with reset and download buttons for chart.
- `type` (String; optional): Chart.js chart type.
- `useGradient` (a value equal to: 'borderColor', 'backgroundColor', 'both'; optional): Apply Linear Gradient on 'borderColor', 'backgroundColor' or on 'both'. Applies on both by default.
"""
function ''_chartjs(; kwargs...)
        available_props = Symbol[:id, :clickData, :customCanvasBackgroundColor, :data, :linearGradientDirection, :linearGradientList, :options, :style, :toolbox, :type, :useGradient]
        wild_props = Symbol[]
        return Component("''_chartjs", "ChartJs", "dash_chartjs", available_props, wild_props; kwargs...)
end

