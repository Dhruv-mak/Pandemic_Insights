from plotly import graph_objs as go
from plotly import express as px
import plotly
import pandas as pd


def get_line_graph_query1(data):
    fig = px.line(
        data,
        x="date",
        y="test_positivity_rate",
        color="country",
        title="Test Positivity Rate Over Time by Country",
    )

    # Use colors that match the dark theme
    dark_bgcolor = "#1e293b"  # Dark gray
    light_text = "#e5e5e5"  # Light gray for text
    grid_color = "#3f3f3f"  # Slightly lighter gray for the grid

    fig.update_layout(
        title={
            "text": "Test Positivity Rate Over Time by Country",
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(color=light_text, size=17),  # Setting title color here
        },
        xaxis_title="Date",
        yaxis_title="Test Positivity Rate",
        xaxis=dict(
            showline=True,
            showgrid=True,  # Set to True to show the gridlines
            showticklabels=True,
            linecolor=light_text,
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color=light_text),
            gridcolor=grid_color,  # Grid color to match the theme
        ),
        yaxis=dict(
            showgrid=True,  # Set to True to show the gridlines
            zeroline=False,
            showline=False,
            showticklabels=True,
            gridcolor=grid_color,  # Grid color to match the theme
            tickfont=dict(color=light_text),  # Tick font color
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor=dark_bgcolor,  # Background color for the plot
        paper_bgcolor=dark_bgcolor,  # Background color for the paper
        font=dict(color=light_text),  # General font color
    )

    # Customize the legend to match the dark theme
    fig.update_layout(legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)))

    return fig


def get_stacked_area_chart(data):
    data["month"] = data["date"].dt.to_period("M")

    # Count 'High Testing' and 'Low Testing' days per month for each country
    monthly_testing_volume = (
        data.groupby(["country", "month", "testing_volume"])
        .size()
        .unstack(fill_value=0)
        .reset_index()
    )

    # Pivot the data for stacked area chart
    pivot_data = monthly_testing_volume.pivot(
        index="month", columns="country", values=["High Testing", "Low Testing"]
    ).fillna(0)

    # Plotly does not directly support stacked area charts with categorical data,
    # so we need to manipulate the data a bit and use 'px.area' for plotting.
    # We create a new DataFrame for plotting
    plot_data = pd.DataFrame(pivot_data.to_records())
    plot_data.columns = [
        hdr.replace("('", "").replace("', '", "_").replace("')", "")
        for hdr in plot_data.columns
    ]
    plot_data["month"] = plot_data["month"].astype(str)

    # Create the stacked area chart
    fig = px.area(
        plot_data,
        x="month",
        y=[
            col
            for col in plot_data.columns
            if col.startswith("High Testing") or col.startswith("Low Testing")
        ],
        title="High Testing vs Low Testing Days Over Time by Country",
        labels={"value": "Number of Days", "variable": "Country and Testing Volume"},
    )

    # Colors for the dark theme
    dark_bgcolor = "#1e293b"  # Dark gray
    light_text = "#e5e5e5"  # Light gray for text
    grid_color = "#3f3f3f"  # Slightly lighter gray for the grid

    # Update layout for dark theme
    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Number of Days",
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor=grid_color,
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color=light_text),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            showticklabels=True,
            gridcolor=grid_color,
            tickfont=dict(color=light_text),
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor=dark_bgcolor,
        paper_bgcolor=dark_bgcolor,
        font=dict(color=light_text),
    )

    # Customize legend and title for the dark theme
    fig.update_layout(
        legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)),
        title=dict(
            text="High Testing vs Low Testing Days Over Time by Country",
            x=0.5,
            xanchor="center",
            yanchor="top",
            font=dict(color=light_text, size=17),
        ),
    )

    return fig


def get_line_graph_testing_quartile(data):
    # Ensure the 'date' column is a datetime type
    data['date'] = pd.to_datetime(data['date'])

    # Create the line graph using Plotly Express
    fig = px.line(
        data,
        x="date",
        y="testing_quartile",
        color="country",
        title="COVID-19 Testing Quartile Over Time by Country",
    )

    # Define colors for a dark theme
    dark_bgcolor = "#1e293b"  # Dark gray
    light_text = "#e5e5e5"  # Light gray for text
    grid_color = "#3f3f3f"  # Slightly lighter gray for the grid

    # Update layout for dark theme
    fig.update_layout(
        title={
            "text": "COVID-19 Testing Quartile Over Time by Country",
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": dict(color=light_text, size=17),  # Setting title color here
        },
        xaxis_title="Date",
        yaxis_title="Testing Quartile",
        xaxis=dict(
            showline=True,
            showgrid=True,  # Set to True to show the gridlines
            showticklabels=True,
            linecolor=light_text,
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color=light_text),
            gridcolor=grid_color,  # Grid color to match the theme
        ),
        yaxis=dict(
            showgrid=True,  # Set to True to show the gridlines
            zeroline=False,
            showline=False,
            showticklabels=True,
            gridcolor=grid_color,  # Grid color to match the theme
            tickfont=dict(color=light_text),  # Tick font color
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor=dark_bgcolor,  # Background color for the plot
        paper_bgcolor=dark_bgcolor,  # Background color for the paper
        font=dict(color=light_text),  # General font color
    )

    # Customize the legend to match the dark theme
    fig.update_layout(legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)))

    return fig
    

def new_cases_smoothed_query1(data):
    fig = px.line(
        data,
        x="date",
        y="new_cases_smoothed",
        color="country",
        title="7-Day Average of New Cases Over Time by Country",
    )

    # Use colors that match the dark theme
    dark_bgcolor = "#1e293b"  # Dark gray
    light_text = "#e5e5e5"  # Light gray for text
    grid_color = "#3f3f3f"  # Slightly lighter gray for the grid

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="7-Day Average of New Cases",
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor=grid_color,
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color=light_text),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            showticklabels=True,
            gridcolor=grid_color,
            tickfont=dict(color=light_text),
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor=dark_bgcolor,
        paper_bgcolor=dark_bgcolor,
        font=dict(color=light_text),
    )

    # Customize legend and title for the dark theme
    fig.update_layout(
        legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)),
        title=dict(
            text="7-Day Average of New Cases Over Time by Country",
            x=0.5,
            xanchor="center",
            yanchor="top",
            font=dict(color=light_text, size=17),
        ),
    )

    return fig


def get_positivity_rate_color_coded_scatter(data):
    fig = px.scatter(
        data,
        x="date",
        y="test_positivity_rate",
        color="country",
        title="Test Positivity Rate Over Time by Country",
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Test Positivity Rate",
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color="rgb(82, 82, 82)"),
        ),
        yaxis=dict(showgrid=True, zeroline=False, showline=False, showticklabels=True),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor="white",
    )
    return fig


def get_animated_heatmap(data):
    # TODO: use this heatmap after fixing the request structure
    # Convert 'date' to datetime and extract year-month for monthly animation
    data["date"] = pd.to_datetime(data["date"])
    data["year_month"] = data["date"].dt.to_period("M").astype(str)

    fig = px.choropleth(
        data,
        locations="country",  # This should be the column name with country names
        locationmode="country names",  # Set location mode to country names
        color="testing_quartile",
        animation_frame="year_month",
        color_continuous_scale="Viridis",
        range_color=[data["testing_quartile"].min(), data["testing_quartile"].max()],
        title="Testing Quartiles Over Time by Country",
    )

    fig.update_layout(
        geo=dict(
            showcountries=True,
            showcoastlines=True,
        ),
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
        autosize=True,
        coloraxis_colorbar=dict(title="Testing Quartile"),
    )

    fig.update_geos(projection_type="natural earth")

    # Add custom play and pause button with increased animation speed
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": 100, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    ),  # Speed up animation
                    dict(
                        label="Pause",
                        method="animate",
                        args=[
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    ),
                ],
                direction="left",
                pad={"r": 10, "t": 87},
                x=0.1,
                xanchor="right",
                y=0,
                yanchor="top",
            )
        ]
    )

    return fig


def get_global_vs_country_trend_line_graph(data, emission_type):
    # Ensure 'year' column is in datetime format for better x-axis formatting
    if data["year"].dtype != "<M8[ns]":  # Check if not already datetime
        data["year"] = pd.to_datetime(data["year"].astype(str))

    # Create the line graph
    fig = px.line(
        data,
        x="year",
        y=emission_type,
        color="country",
        title=f"{emission_type.replace('_', ' ').title()} Over Time by Country vs Global",
    )

    # Colors for the dark theme
    dark_bgcolor = "#1e293b"  # Dark gray
    light_text = "#e5e5e5"  # Light gray for text
    grid_color = "#3f3f3f"  # Slightly lighter gray for the grid

    # Update layout for dark theme
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title=emission_type.replace("_", " ").title(),
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor=grid_color,
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color=light_text),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            showticklabels=True,
            gridcolor=grid_color,
            tickfont=dict(color=light_text),
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor=dark_bgcolor,
        paper_bgcolor=dark_bgcolor,
        font=dict(color=light_text),
    )

    # Customize legend and title for the dark theme
    fig.update_layout(
        legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)),
        title=dict(
            text=f"{emission_type.replace('_', ' ').title()} Over Time by Country vs Global",
            x=0.5,
            xanchor="center",
            yanchor="top",
            font=dict(size=17, color=light_text),
        ),
    )

    return fig


def get_line_graph_new_deaths_smoothed(data):
    fig = px.line(
        data,
        x="date",
        y="new_deaths_smoothed_per_million",
        color="location",
        title="New Deaths Smoothed Per Million Over Time by Country",
    )

    # Define colors for a dark theme
    dark_bgcolor = "#1e293b"  # Dark gray background
    light_text = "#e5e5e5"  # Light gray text
    grid_color = "#3f3f3f"  # Slightly lighter gray for grid lines

    # Update layout with dark theme colors
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="New Deaths Smoothed Per Million",
        xaxis=dict(
            showline=True,
            showgrid=True,  # Enable grid
            showticklabels=True,
            linecolor=light_text,
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color=light_text),
            gridcolor=grid_color,  # Set grid color
        ),
        yaxis=dict(
            showgrid=True,  # Enable grid
            zeroline=False,
            showline=False,
            showticklabels=True,
            gridcolor=grid_color,  # Set grid color
            tickfont=dict(color=light_text),
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor=dark_bgcolor,  # Set plot background color
        paper_bgcolor=dark_bgcolor,  # Set paper background color
        font=dict(color=light_text),  # Set font color
    )

    # Customize the legend and title for the dark theme
    fig.update_layout(
        legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)),
        title=dict(
            text="New Deaths Smoothed Per Million Over Time by Country",
            x=0.5,
            xanchor="center",
            yanchor="top",
            font=dict(size=17, color=light_text),
        ),
    )

    return fig


def get_interaction_graph(data, interaction_metric):
    if interaction_metric not in data.columns:
        raise ValueError(f"Interaction metric '{interaction_metric}' not found in data")

    # Define colors for a dark theme
    dark_bgcolor = "#1e293b"  # Dark gray background
    light_text = "#e5e5e5"  # Light gray text
    grid_color = "#3f3f3f"  # Slightly lighter gray for grid lines

    fig = px.line(
        data,
        x="date",
        y=interaction_metric,
        color="location",
        title=f'{interaction_metric.replace("_", " ").title()} Over Time by Country',
    )

    # Update layout with dark theme colors
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title=interaction_metric.replace("_", " ").title(),
        xaxis=dict(
            showline=True,
            showgrid=True,  # Enable grid
            showticklabels=True,
            linecolor=light_text,
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color=light_text),
            gridcolor=grid_color,  # Set grid color
        ),
        yaxis=dict(
            showgrid=True,  # Enable grid
            zeroline=False,
            showline=False,
            showticklabels=True,
            gridcolor=grid_color,  # Set grid color
            tickfont=dict(color=light_text),
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor=dark_bgcolor,  # Set plot background color
        paper_bgcolor=dark_bgcolor,  # Set paper background color
        font=dict(color=light_text),  # Set font color
    )

    # Customize the legend and title for the dark theme
    fig.update_layout(
        legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)),
        title=dict(
            text=f'{interaction_metric.replace("_", " ").title()} Over Time by Country',
            x=0.5,
            xanchor="center",
            yanchor="top",
            font=dict(size=17, color=light_text),
        ),
    )

    return fig


def get_metric_rank_graph(data, metric):
    # Assuming the data already contains a ranking column for the metric.
    # For example, 'gdp_rank' for GDP-related rankings.
    rank_column = f"{metric}_rank"

    if rank_column not in data.columns:
        raise ValueError(f"Rank column '{rank_column}' not found in data")

    # Sort data based on date and rank
    sorted_data = data.sort_values(by=["date", rank_column])

    fig = px.bar(
        sorted_data,
        x="date",
        y=rank_column,
        color="location",
        title=f'Ranking of Countries by {metric.replace("_", " ").title()} Over Time',
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title=f'Rank for {metric.replace("_", " ").title()}',
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color="rgb(82, 82, 82)"),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            showticklabels=True,
            autorange="reversed",
        ),  # Reverse y-axis to show rank 1 at top
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor="white",
    )

    return fig


def get_line_graph(data, metric):
    # Ensure the data is sorted correctly
    data = data.sort_values(by=["country", "year"])

    # Determine the title based on the metric
    title = (
        "Human Development Index (HDI) Over Time by Country"
        if metric == "hdi"
        else "Gender Inequality Index (GII) Over Time by Country"
    )

    # Create the line graph
    fig = px.line(
        data,
        x="year",
        y=metric,
        color="country",
        title=title,
    )

    # Define colors for a dark theme
    dark_bgcolor = "#1e293b"  # Dark gray background
    light_text = "#e5e5e5"  # Light gray text
    grid_color = "#3f3f3f"  # Slightly lighter gray for grid lines

    # Update layout with dark theme colors
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title=(
            "Human Development Index (HDI)"
            if metric == "hdi"
            else "Gender Inequality Index (GII)"
        ),
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor=grid_color,
            linewidth=2,
            ticks="outside",
            tickfont=dict(family="Arial", size=12, color=light_text),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=False,
            showticklabels=True,
            gridcolor=grid_color,
            tickfont=dict(color=light_text),
        ),
        autosize=True,
        margin=dict(autoexpand=True),
        showlegend=True,
        plot_bgcolor=dark_bgcolor,
        paper_bgcolor=dark_bgcolor,
        font=dict(color=light_text),
    )

    # Customize the legend and title for the dark theme
    fig.update_layout(
        legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)),
        title=dict(
            text=title,
            x=0.5,
            xanchor="center",
            yanchor="top",
            font=dict(size=17, color=light_text),
        ),
    )

    return fig


from plotly.subplots import make_subplots


def plot_dual_axis_line_graph(data):
    # Define colors for a dark theme
    dark_bgcolor = "#1e293b"  # Dark gray background
    light_text = "#e5e5e5"  # Light gray text
    grid_color = "#3f3f3f"  # Slightly lighter gray for grid lines

    # Create a figure with secondary y-axis using make_subplots
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Iterate through each country to plot its data
    for country in data["country"].unique():
        country_data = data[data["country"] == country]

        # Add lagged excess mortality line
        fig.add_trace(
            go.Scatter(
                x=country_data["date"],
                y=country_data["lagged_excess_mortality"],
                name=f"{country} - Lagged Excess Mortality",
                mode="lines",
            ),
            secondary_y=False,
        )

        # Add lagged vaccination rate line
        fig.add_trace(
            go.Scatter(
                x=country_data["date"],
                y=country_data["lagged_vaccination_rate"],
                name=f"{country} - Lagged Vaccination Rate",
                mode="lines",
            ),
            secondary_y=True,
        )

    # Update the layout for the dark theme
    fig.update_layout(
        paper_bgcolor=dark_bgcolor,
        plot_bgcolor=dark_bgcolor,
        font_color=light_text,
        title={
            "text": "Lagged Excess Mortality and Vaccination Rate Over Time by Country",
            "y": 0.9,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
        },
        xaxis=dict(
            title="Date",
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor=light_text,
            gridcolor=grid_color,
            tickfont=dict(color=light_text),
        ),
        xaxis2=dict(
            title="Date",
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor=light_text,
            gridcolor=grid_color,
            tickfont=dict(color=light_text),
            overlaying="x",
            side="top",
        ),
        yaxis=dict(
            title="Lagged Excess Mortality",
            showgrid=True,
            gridcolor=grid_color,
        ),
        yaxis2=dict(
            title="Lagged Vaccination Rate",
            overlaying="y",
            side="right",
            showgrid=False,
        ),
        legend=dict(bgcolor=dark_bgcolor, font=dict(color=light_text)),
    )

    # Customize y-axis for the dark theme
    fig.update_yaxes(
        title_text="Lagged Excess Mortality",
        secondary_y=False,
        gridcolor=grid_color,
        tickfont=dict(color=light_text),
    )
    fig.update_yaxes(
        title_text="Lagged Vaccination Rate", secondary_y=True, showgrid=False
    )

    return fig

def generate_gii_heatmap(data):
    # Convert year to string to work with plotly express
    data['year'] = data['year'].astype(str)

    fig = px.choropleth(
        data,
        locations="country",
        locationmode="country names",
        color="gii",
        hover_name="country",
        animation_frame="year",
        range_color=[data['gii'].min(), data['gii'].max()],
        color_continuous_scale=px.colors.sequential.Plasma,
        title="Global Human Development Index (HDI) Over Time",
    )

    # Update layout for a better visual appearance
    fig.update_layout(
        margin={"r":0,"t":50,"l":0,"b":0},
        paper_bgcolor="#1f1f1f",
        geo=dict(
            bgcolor= 'rgba(0,0,0,0)',
            lakecolor='rgba(0,0,0,0)',
            landcolor='rgba(0,0,0,0)',
            subunitcolor='rgb(100,100,100)'
        ),
        coloraxis_colorbar=dict(
            title="GII",
            tickvals=[0, 0.5, 1],
            ticktext=["Low", "Medium", "High"],
        ),
    )

    # Remove the default animation bar and play button
    fig.layout.updatemenus = [dict(
        type="buttons",
        showactive=False,
        buttons=[dict(label="Play", method="animate", args=[None, {"frame": {"duration": 0, "redraw": False}, "fromcurrent": True}])]
    )]

    return fig