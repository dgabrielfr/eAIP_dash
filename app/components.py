"""
Dash components required for the app
"""
from dash import html
import dash_mantine_components as dmc


def get_top_part():
    """
    Provide the top part of the app
    """
    return dmc.SimpleGrid(
        cols=2,
        children=[
            dmc.Text("Browse to AIRAC_date.txt:"),
            dmc.Button("bla"),
            dmc.Text("Enter the folder path:"),
            dmc.TextInput("-"),
            dmc.Progress(12),
            dmc.Button("Download")
        ]
    )

def get_bottom_part():
    """
    Provide the bottom part of the app
    """
    return html.Div(
    children=[
        dmc.Space(h="xl"),
        dmc.Text("AIRAC info...")
    ],
    style=dict(display='flex', justifyContent='center')
)
