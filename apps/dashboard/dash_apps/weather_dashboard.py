import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django_plotly_dash import DjangoDash

app = DjangoDash('WeatherDashboard')

def get_sample_weather_data():
    return pd.DataFrame({
        'city': ['New York', 'London', 'Tokyo', 'Sydney'] * 6,
        'temperature': [22, 15, 28, 25, 21, 14, 27, 24, 23, 16, 29, 26,
                       20, 13, 26, 23, 22, 15, 28, 25, 24, 17, 30, 27],
        'humidity': [65, 72, 68, 45, 63, 75, 65, 42, 67, 78, 62, 40,
                    70, 80, 60, 38, 68, 76, 63, 41, 65, 74, 61, 39],
        'timestamp': pd.date_range('2024-01-01', periods=24, freq='H')
    })

df = get_sample_weather_data()

app.layout = html.Div([
    html.H1("Weather Monitoring Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            html.Div([
                html.H3("Current Temp", style={'color': '#ffffff'}),
                html.H2("22°C", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#3498DB', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-3'),
        
        html.Div([
            html.Div([
                html.H3("Humidity", style={'color': '#ffffff'}),
                html.H2("65%", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#27AE60', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-3'),
        
        html.Div([
            html.Div([
                html.H3("Pressure", style={'color': '#ffffff'}),
                html.H2("1013 hPa", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#E74C3C', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-3'),
        
        html.Div([
            html.Div([
                html.H3("Wind Speed", style={'color': '#ffffff'}),
                html.H2("3.5 m/s", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#F39C12', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-3'),
    ], className='row', style={'marginBottom': '20px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='temperature-trend',
                figure=px.line(df, x='timestamp', y='temperature', color='city',
                             title='Temperature Trends by City',
                             labels={'temperature': 'Temperature (°C)', 'timestamp': 'Time'})
            )
        ], className='col-md-6'),
        
        html.Div([
            dcc.Graph(
                id='humidity-chart',
                figure=px.bar(df[df['timestamp'] == df['timestamp'].max()], 
                            x='city', y='humidity',
                            title='Current Humidity by City',
                            labels={'humidity': 'Humidity (%)', 'city': 'City'})
            )
        ], className='col-md-6'),
    ], className='row'),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='weather-map',
                figure=go.Figure(go.Scattergeo(
                    lon = [-74.006, -0.1278, 139.6917, 151.2093],
                    lat = [40.7128, 51.5074, 35.6895, -33.8688],
                    text = ['New York', 'London', 'Tokyo', 'Sydney'],
                    mode = 'markers',
                    marker = dict(
                        size = 20,
                        color = [22, 15, 28, 25],
                        colorscale = 'Viridis',
                        showscale = True,
                        colorbar_title = "Temp (°C)"
                    )
                )).update_layout(
                    title = 'Global Weather Stations',
                    geo_scope='world'
                )
            )
        ], className='col-md-12'),
    ], className='row'),
    
    dcc.Interval(
        id='interval-component',
        interval=5*60*1000,  # Update every 5 minutes
        n_intervals=0
    )
])
