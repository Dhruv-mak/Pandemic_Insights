from plotly import graph_objs as go
from plotly import express as px
import plotly
import pandas as pd

def get_line_graph_query1(data):
    fig = px.line(data, x='date', y='test_positivity_rate', color='country', 
                    title='Test Positivity Rate Over Time by Country')

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Test Positivity Rate',
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')),
        yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=True),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor='white'
    )
    
    return fig

def get_stacked_area_chart(data):
    data['month'] = data['date'].dt.to_period('M')

    # Count 'High Testing' and 'Low Testing' days per month for each country
    monthly_testing_volume = data.groupby(['country', 'month', 'testing_volume']).size().unstack(fill_value=0).reset_index()

    # Pivot the data for stacked area chart
    pivot_data = monthly_testing_volume.pivot(index='month', columns='country', values=['High Testing', 'Low Testing']).fillna(0)

    # Plotly does not directly support stacked area charts with categorical data,
    # so we need to manipulate the data a bit and use 'px.area' for plotting.
    # We create a new DataFrame for plotting
    plot_data = pd.DataFrame(pivot_data.to_records())
    plot_data.columns = [hdr.replace("('", "").replace("', '", "_").replace("')", "") for hdr in plot_data.columns]
    plot_data['month'] = plot_data['month'].astype(str)

    # Create the stacked area chart
    fig = px.area(plot_data, 
                x='month', 
                y=[col for col in plot_data.columns if col.startswith('High Testing') or col.startswith('Low Testing')],
                title='High Testing vs Low Testing Days Over Time by Country',
                labels={'value': 'Number of Days', 'variable': 'Country and Testing Volume'})

    # Update layout
    fig.update_layout(
        xaxis_title='Month',
        yaxis_title='Number of Days',
        xaxis=dict(showline=True, showgrid=True, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')),
        yaxis=dict(showgrid=True, zeroline=False, showline=False, showticklabels=True),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor='white'
    )
    return fig

def get_percentile_graph_query1(data):
    fig = px.line(data, x='date', y='testing_volume', color='testing_quartile', line_group='country',
              title='Testing Volume Over Time by Quartile for Each Country',
              labels={'date': 'Date', 'testing_volume': 'Testing Volume', 'testing_quartile': 'Testing Quartile', 'country': 'Country'},
              category_orders={"testing_quartile": [1, 2, 3, 4]})  # Ensures quartiles are in order

    # Update layout for better readability
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Testing Volume',
        xaxis=dict(showline=True, showgrid=True, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')),
        yaxis=dict(showgrid=True, zeroline=False, showline=False, showticklabels=True),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor='white'
    )
    return fig

def new_cases_smoothed_query1(data):
    fig = px.line(data, x='date', y='new_cases_smoothed', color='country',
                  title='7-Day Average of New Cases Over Time by Country')

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='7-Day Average of New Cases',
        xaxis=dict(showline=True, showgrid=True, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')),
        yaxis=dict(showgrid=True, zeroline=False, showline=False, showticklabels=True),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor='white'
    )
    return fig

def get_positivity_rate_color_coded_scatter(data):
    fig = px.scatter(data, x='date', y='test_positivity_rate', color='country',
                        title='Test Positivity Rate Over Time by Country')
    
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Test Positivity Rate',
        xaxis=dict(showline=True, showgrid=True, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')),
        yaxis=dict(showgrid=True, zeroline=False, showline=False, showticklabels=True),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor='white'
    )
    return fig


def get_animated_heatmap(data):
    # TODO: use this heatmap after fixing the request structure
    # Convert 'date' to datetime and extract year-month for monthly animation
    data['date'] = pd.to_datetime(data['date'])
    data['year_month'] = data['date'].dt.to_period('M').astype(str)

    fig = px.choropleth(
        data,
        locations='country',  # This should be the column name with country names
        locationmode='country names',  # Set location mode to country names
        color='testing_quartile',
        animation_frame='year_month',
        color_continuous_scale='Viridis',
        range_color=[data['testing_quartile'].min(), data['testing_quartile'].max()],
        title='Testing Quartiles Over Time by Country'
    )

    fig.update_layout(
        geo=dict(
            showcountries=True,
            showcoastlines=True,
        ),
        margin={"r":0,"t":30,"l":0,"b":0},
        autosize=True,
        coloraxis_colorbar=dict(title='Testing Quartile')
    )

    fig.update_geos(projection_type="natural earth")

    # Add custom play and pause button with increased animation speed
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(label="Play", method="animate",
                         args=[None, {"frame": {"duration": 100, "redraw": True}, "fromcurrent": True}]),  # Speed up animation
                    dict(label="Pause", method="animate",
                         args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}])
                ],
                direction="left",
                pad={"r": 10, "t": 87},
                x=0.1,
                xanchor="right",
                y=0,
                yanchor="top"
            )
        ]
    )

    return fig

def get_global_vs_country_trend_line_graph(data, emission_type):
    # Ensure 'year' column is in datetime format for better x-axis formatting
    if data['year'].dtype != '<M8[ns]':  # Check if not already datetime
        data['year'] = pd.to_datetime(data['year'].astype(str))
    # Create the line graph
    fig = px.line(data, x='year', y=emission_type, color='country',
                  title=f'{emission_type} Over Time by Country vs Global')

    # Update layout for better readability
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title=emission_type.replace('_', ' ').title(),
        xaxis=dict(showline=True, showgrid=False, showticklabels=True, linecolor='rgb(204, 204, 204)', linewidth=2, ticks='outside', tickfont=dict(family='Arial', size=12, color='rgb(82, 82, 82)')),
        yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=True),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor='white'
    )

    return fig