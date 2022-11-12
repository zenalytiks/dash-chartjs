# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''ChartJs <- function(id=NULL, clickData=NULL, data=NULL, options=NULL, style=NULL, type=NULL) {
    
    props <- list(id=id, clickData=clickData, data=data, options=options, style=style, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ChartJs',
        namespace = 'dash_chartjs',
        propNames = c('id', 'clickData', 'data', 'options', 'style', 'type'),
        package = 'dashChartjs'
        )

    structure(component, class = c('dash_component', 'list'))
}
