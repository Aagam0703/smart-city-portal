import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django_plotly_dash import DjangoDash

app = DjangoDash('ServicesDashboard')

def get_sample_services_data():
    return pd.DataFrame({
        'service_type': ['Sanitation', 'Transportation', 'Utilities', 'Public Safety', 'Other'] * 4,
        'requests': [45, 38, 52, 29, 16, 42, 35, 48, 31, 12, 38, 40, 45, 27, 14, 50, 42, 55, 33, 18],
        'status': ['Open']*5 + ['In Progress']*5 + ['Completed']*5 + ['Closed']*5,
        'response_time': [2.1, 1.8, 3.2, 0.5, 2.8, 1.5, 1.2, 2.8, 0.8, 2.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    })

df = get_sample_services_data()

app.layout = html.Div([
    html.H1("City Services Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        html.Div([
            html.Div([
                html.H3("Open Requests", style={'color': '#ffffff'}),
                html.H2("156", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#E74C3C', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-3'),
        
        html.Div([
            html.Div([
                html.H3("In Progress", style={'color': '#ffffff'}),
                html.H2("89", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#F39C12', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-3'),
        
        html.Div([
            html.Div([
                html.H3("Completed Today", style={'color': '#ffffff'}),
                html.H2("67", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#27AE60', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-3'),
        
        html.Div([
            html.Div([
                html.H3("Avg Response", style={'color': '#ffffff'}),
                html.H2("2.1h", style={'color': '#ffffff', 'fontSize': '2.5em'})
            ], className='card', style={'backgroundColor': '#3498DB', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center'}),
        ], className='col-md-3'),
    ], className='row', style={'marginBottom': '20px'}),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='requests-by-type',
                figure=px.pie(df[df['status'] == 'Open'], 
                            values='requests', names='service_type',
                            title='Open Requests by Service Type')
            )
        ], className='col-md-6'),
        
        html.Div([
            dcc.Graph(
                id='requests-by-status',
                figure=px.bar(df.groupby('status')['requests'].sum().reset_index(),
                            x='status', y='requests',
                            title='Total Requests by Status',
                            labels={'requests': 'Number of Requests', 'status': 'Status'})
            )
        ], className='col-md-6'),
    ], className='row'),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id='response-times',
                figure=px.box(df[df['response_time'] > 0], 
                            x='service_type', y='response_time',
                            title='Response Times by Service Type (Hours)',
                            labels={'response_time': 'Response Time (hours)', 'service_type': 'Service Type'})
            )
        ], className='col-md-12'),
    ], className='row'),
    
    dcc.Interval(
        id='interval-component',
        interval=2*60*1000,  # Update every 2 minutes
        n_intervals=0
    )
])
