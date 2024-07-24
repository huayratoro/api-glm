import plotly.express as px
import pandas as pd

px.set_mapbox_access_token("pk.eyJ1IjoiaHVheXJhdG9ybyIsImEiOiJjbDh2b3B4NGwwMGZxM3dycWpmcGl2OHk0In0.0O1T59GQ4Osmoi3hfIsAgA")

db = pd.read_csv("eventos.csv")

fig = px.scatter_mapbox(
    db,
    lat="event_lat",
    lon="event_lon",
    center={
        "lat": db.event_lat.mean(),
        "lon": db.event_lon.mean()
    },
    zoom=4, mapbox_style="classic"
)

fig.show()

# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd
# px.set_mapbox_access_token("pk.eyJ1IjoiaHVheXJhdG9ybyIsImEiOiJjbDh2b3B4NGwwMGZxM3dycWpmcGl2OHk0In0.0O1T59GQ4Osmoi3hfIsAgA")

# db = pd.read_csv("eventos.csv")

# ## creo la app
# app = dash.Dash(__name__)

# ## creo el layout de la app
# app.layout = html.Div([
#     html.H1("Visualizacion de lugares de descargas electricas"),
#     html.Div([
#         dcc.Graph(id='scatter-plot')
#     ])
# ], style={"height": "100vh"})

# ## defino el callback
# @app.callback(
#     Output('scatter-plot', 'figura'),
#     Input('')
# )

# def grafica():
#     fig = px.scatter_mapbox(
#         db,
#         lat="event_lat",
#         lon="evento_lon",
#         center={
#             "lat": db.event_lat.mean(),
#             "lon": db.event_lon.mean()
#         },
#         zoom=4, mapbox_style="stamen-terrain"
#     )

#     return fig

# if __name__ == '__main__':
#     app.run_server(debug=True)