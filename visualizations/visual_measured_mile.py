import plotly.express as px


def productivity_chart(df):

    fig = px.bar(
        df,
        x="Period",
        y="Productivity",
        color="Type",
        barmode="group",
        title="Measured Mile vs Impacted Productivity"
    )

    fig.update_layout(
        xaxis_title="Period",
        yaxis_title="Productivity",
        legend_title="Period Type"
    )

    return fig