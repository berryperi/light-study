import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

df = pd.read_csv('result_0625.csv', encoding='cp949')

fig = px.bar(df, x="지점", y="판매량", color="상품타입")

app.layout = html.Div(children=[
    html.H1(children='Dsah Board'),

    html.Div(children='''
        작업 대쉬 보드 
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)