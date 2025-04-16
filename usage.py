from dash import Dash, html
import dash_bootstrap_components as dbc
from examples.line_chart import chart as line
from examples.pie_chart import chart as pie
from examples.radar_chart import chart as radar
from examples.combined_line_bar_chart import chart as combined_line_bar
from examples.choropleth_map import chart as choropleth
from examples.pcp_chart import chart as pcp
from examples.matrix_chart import chart as matrix
from examples.boxplot_chart import chart as boxplot
from examples.treemap_chart import chart as treemap
from examples.sankey_chart import chart as sankey
from examples.forced_directed_graph import chart as graph



app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])



app.layout = dbc.Container([
    html.H1('Dash ChartJs Component',className='text-center'),
    
    dbc.Row(
      [
          line,
          pie,
          radar,
          combined_line_bar,
          choropleth,
          pcp,
          matrix,
          boxplot,
          treemap,
          sankey,
          graph
      ]
    )
      
    
])
    


if __name__ == '__main__':
    app.run(debug=True)
