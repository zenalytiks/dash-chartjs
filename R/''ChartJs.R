# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''ChartJs <- function(id=NULL, actions=NULL, clickData=NULL, customJSFunctions=NULL, customPlugins=NULL, data=NULL, options=NULL, redraw=NULL, style=NULL, toolbox=NULL, type=NULL) {
    
    props <- list(id=id, actions=actions, clickData=clickData, customJSFunctions=customJSFunctions, customPlugins=customPlugins, data=data, options=options, redraw=redraw, style=style, toolbox=toolbox, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ChartJs',
        namespace = 'dash_chartjs',
        propNames = c('id', 'actions', 'clickData', 'customJSFunctions', 'customPlugins', 'data', 'options', 'redraw', 'style', 'toolbox', 'type'),
        package = 'dashChartjs'
        )

    structure(component, class = c('dash_component', 'list'))
}
