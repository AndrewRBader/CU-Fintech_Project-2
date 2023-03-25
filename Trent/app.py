from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from pathlib import Path
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/AndrewRBader/CU-Fintech_Project-2/main/Resources/spotify_us_df.csv')
columns_list = list(df.columns)

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                columns_list,
                'Artist',
                id='xaxis-column'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                columns_list,
                'Popularity',
                id='yaxis-column'
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value')
)
    
def update_graph(xaxis_column_name, yaxis_column_name):
    dff = df

    fig = px.scatter(x=dff[xaxis_column_name],
                     y=dff[yaxis_column_name]
                     )

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')


    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
