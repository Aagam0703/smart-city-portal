import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django_plotly_dash import DjangoDash

app = DjangoDash('CityStatsDashboard')

def get_sample_city_data():
    return pd.DataFrame({
        'indicator': ['Population', 'Area (km²)', 'Density', 'GDP Growth', 'Unemployment', 'Crime Rate'] * 2,
        'value': [8.4, 783.8, 10641, 2.3, 4.1, 2.8, 8.5, 784.2, 10841, 2.5, 3.9, 2.7],
        'year': [2023]*6 + [2024]*6,
        'target': [8.8, 800, 11000, 3.0, 3.5, 2.5, 8.8, 800, 11000, 3.0, 3.5, 2.5]
    })

df = get_sample_city_data()

app.layout = html.Div([
    html.H1("City Statistics Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            html.Div([
                html.H3("Population", style={'color': '#ffffff'}),
                html.H2("8.5M", style={'color': '#ffffff', 'fontSize': '2.5em'}),
                html.P("+1.2% YoY", style={'color': '#ffffff', 'margin': 0})
            ], className='card', style={'backgroundColor': '#2C3E50', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-4'),
        
        html.Div([
            html.Div([
                html.H3("GDP Growth", style={'color': '#ffffff'}),
                html.H2("2.5%", style={'color': '#ffffff', 'fontSize': '2.5em'}),
                html.P("+0.2% QoQ", style={'color': '#ffffff', 'margin': 0})
            ], className='card', style={'backgroundColor': '#27AE60', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-4'),
        
        html.Div([
            html.Div([
                html.H3("Unemployment", style={'color': '#ffffff'}),
                html.H2("3.9%", style={'color': '#ffffff', 'fontSize': '2.5em'}),
                html.P("-0.2% YoY", style={'color': '#ffffff', 'margin': 0})
            ], className='card', style={'backgroundColor': '#E74C3C', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-4'),
    ], className='row', style={'marginBottom': '20px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='kpi-trends',
                figure=px.line(df, x='year', y='value', color='indicator',
                             title='Key Performance Indicators Over Time',
                             labels={'value': 'Value', 'year': 'Year', 'indicator': 'Indicator'})
            )
        ], className='col-md-8'),
        
        html.Div([
            dcc.Graph(
                id='target-achievement',
                figure=go.Figure(data=[
                    go.Bar(name='Current', 
                          x=df[df['year'] == 2024]['indicator'], 
                          y=df[df['year'] == 2024]['value']),
                    go.Bar(name='Target', 
                          x=df[df['year'] == 2024]['indicator'], 
                          y=df[df['year'] == 2024]['target'])
                ]).update_layout(
                    title='Current vs Target Values (2024)',
                    barmode='group'
                )
            )
        ], className='col-md-4'),
    ], className='row'),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='progress-gauge',
                figure=go.Figure(go.Indicator(
                    mode = "gauge+number+delta",
                    value = 85,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "Overall City Goals Progress"},
                    delta = {'reference': 80},
                    gauge = {
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 50], 'color': "lightgray"},
                            {'range': [50, 80], 'color': "gray"}],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 90}}
                )).update_layout(height=300)
            )
        ], className='col-md-6'),
        
        html.Div([
            dcc.Graph(
                id='city-map',
                figure=px.choropleth(locations=["New York"], 
                                   locationmode="USA-states",
                                   color=[1],
                                   scope="usa",
                                   title="City Boundary Map",
                                   color_continuous_scale="Blues")
            )
        ], className='col-md-6'),
    ], className='row'),
    
    dcc.Interval(
        id='interval-component',
        interval=10*60*1000,  # Update every 10 minutes
        n_intervals=0
    )
])
