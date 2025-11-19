import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django_plotly_dash import DjangoDash

app = DjangoDash('TransitDashboard')

# Sample data - replace with actual data from your models
def get_sample_transit_data():
    return pd.DataFrame({
        'hour': list(range(24)),
        'subway_delays': [5, 3, 2, 1, 1, 2, 8, 15, 12, 10, 8, 7, 6, 5, 4, 6, 10, 12, 9, 7, 6, 5, 4, 3],
        'bus_delays': [2, 1, 1, 0, 0, 1, 5, 12, 18, 15, 12, 10, 8, 7, 6, 8, 14, 16, 13, 10, 8, 6, 4, 3],
        'avg_wait_time': [8, 7, 6, 5, 5, 6, 4, 3, 5, 6, 5, 4, 4, 4, 4, 5, 6, 7, 6, 5, 5, 6, 7, 8]
    })

df = get_sample_transit_data()

app.layout = html.Div([
    html.H1("Public Transit Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            html.Div([
                html.H3("Subway Delays", style={'color': '#ffffff'}),
                html.H2("15", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#2E86AB', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-4'),
        
        html.Div([
            html.Div([
                html.H3("Bus Delays", style={'color': '#ffffff'}),
                html.H2("12", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#A23B72', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-4'),
        
        html.Div([
            html.Div([
                html.H3("Avg Wait Time", style={'color': '#ffffff'}),
                html.H2("4.2 min", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#F18F01', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-4'),
    ], className='row', style={'marginBottom': '20px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='delays-by-hour',
                figure=px.line(df, x='hour', y=['subway_delays', 'bus_delays'],
                             title='Delays by Hour of Day',
                             labels={'value': 'Number of Delays', 'hour': 'Hour', 'variable': 'Transport Type'})
            )
        ], className='col-md-6'),
        
        html.Div([
            dcc.Graph(
                id='wait-times',
                figure=px.bar(df, x='hour', y='avg_wait_time',
                            title='Average Wait Times by Hour',
                            labels={'avg_wait_time': 'Wait Time (min)', 'hour': 'Hour'})
            )
        ], className='col-md-6'),
    ], className='row'),
    
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # Update every minute
        n_intervals=0
    )
])
