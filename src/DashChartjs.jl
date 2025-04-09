
module DashChartjs
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "1.0.0"

include("jl/''_chartjs.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_chartjs",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_chartjs.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_chartjs.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
