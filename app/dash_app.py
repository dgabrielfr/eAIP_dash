"""
Dash app entry point
"""

from dash import Dash
import dash_mantine_components as dmc
from dash import _dash_renderer
_dash_renderer._set_react_version("18.2.0")

from components import get_bottom_part, get_top_part


app = Dash()

app.layout = dmc.MantineProvider(children=dmc.Stack([
    get_top_part(),
    get_bottom_part()
]))

if __name__ == '__main__':
    app.run(debug=True)
