from email import header

import dash

from dash.dependencies import Input, Output

from dash import dcc

from dash import html

from pandas_datareader import data as web

from datetime import datetime as dt

app = dash.Dash()

app.layout = html.Div([
                dcc.Dropdown(

                    id="dropdown",
                    options=[
                        {'label':'Google', 'value': 'Alphabet Inc.'},
                        {'label':'Apple', 'value': 'AAPL'},
                        {'label':'Microsoft', 'value': 'MSFT'},
                        {'label':'Tesla', 'value': 'TSLA'},
                        {'label':'NVIDIA', 'value': 'NVDA'},
                        {'label':'QUALCOMM Incorporated', 'value': 'QCOM'},
                        {'label':'Broadcom Inc.', 'value': 'AVGO'}, 
                        {'label':'Advanced Micro Devices, Inc.', 'value': 'AMD'}, 
                        {'label':'Zoom Video Communications, Inc.', 'value': 'ZM'},
                        {'label':'Autodesk, Inc.', 'value': 'ADSK'}, 
                        {'label':'Texas Instruments Incorporated', 'value': 'TXN'},
                        {'label':'Intuit Inc.', 'value': 'INTU'}, 
                        {'label':'Match Group, Inc', 'value': 'MTCH'},
                        {'label':'Micron Technology, Inc.', 'value': 'MU'}, 
                        {'label':'Palo Alto Networks, Inc.', 'value': 'PANW'},
                        {'label':'Okta, Inc', 'value': 'OKTA'}, 
                        {'label':'CrowdStrike Holdings, Inc.', 'value': 'CRWD'},    
                    ],
                ),
                dcc.Graph(id="graph")


], style={'width':'300'})

#Callback Decorator
@app.callback(Output('graph', 'figure'), [Input('dropdown', 'value')])
def graph(selected_dropdown_value):
    df = web.DataReader(selected_dropdown_value, 'yahoo', dt(2015, 1, 1), dt.now())
    return {
        'data': [ { 'x' : df.index,
                    'y' : df.Close }],
        'layout' : {'margin': {'l':40, 'r':0, 't':60, 'b':30}}    
    }


if __name__ == "__main__":
    app.run_server(debug=True)