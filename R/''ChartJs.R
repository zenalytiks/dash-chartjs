# AUTO GENERATED FILE - DO NOT EDIT

#' @export
''ChartJs <- function(id=NULL, data=NULL, options=NULL, type=NULL) {
    
    props <- list(id=id, data=data, options=options, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ChartJs',
        namespace = 'dash_chartjs',
        propNames = c('id', 'data', 'options', 'type'),
        package = 'dashChartjs'
        )

    structure(component, class = c('dash_component', 'list'))
}
