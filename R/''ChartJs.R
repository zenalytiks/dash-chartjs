# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''ChartJs <- function(id=NULL, clickData=NULL, customCanvasBackgroundColor=NULL, data=NULL, linearGradientDirection=NULL, linearGradientList=NULL, options=NULL, style=NULL, toolbox=NULL, type=NULL, useGradient=NULL) {
    
    props <- list(id=id, clickData=clickData, customCanvasBackgroundColor=customCanvasBackgroundColor, data=data, linearGradientDirection=linearGradientDirection, linearGradientList=linearGradientList, options=options, style=style, toolbox=toolbox, type=type, useGradient=useGradient)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ChartJs',
        namespace = 'dash_chartjs',
        propNames = c('id', 'clickData', 'customCanvasBackgroundColor', 'data', 'linearGradientDirection', 'linearGradientList', 'options', 'style', 'toolbox', 'type', 'useGradient'),
        package = 'dashChartjs'
        )

    structure(component, class = c('dash_component', 'list'))
}
