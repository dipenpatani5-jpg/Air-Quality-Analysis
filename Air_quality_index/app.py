
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="Air Quality Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------
# LOAD DATASET
# ---------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("Cleaned_AirQuality.csv")

    df["Date"] = pd.to_datetime(
        df["Date"], utc=True, errors="coerce"
    ).dt.tz_convert(None)

    df["Value"] = pd.to_numeric(
        df["Value"], errors="coerce"
    )

    df = df.dropna(
        subset=["Date", "Value", "Pollutant", "Location"]
    )

    return df

df = load_data()

# ---------------------------------
# DASHBOARD TITLE
# ---------------------------------

st.title("🌍 Air Quality Analysis Dashboard")

st.markdown(
    "### Monitor pollution levels across different locations"
)

st.markdown("---")

# ---------------------------------
# SIDEBAR FILTERS
# ---------------------------------

st.sidebar.header("Dashboard Filters")

pollutants = sorted(df["Pollutant"].unique())

selected_pollutant = st.sidebar.selectbox(
    "Select Pollutant",
    pollutants
)

locations = sorted(df["Location"].unique())

selected_locations = st.sidebar.multiselect(
    "Select Locations",
    locations,
    default=locations
)

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# ---------------------------------
# FILTER DATA
# ---------------------------------

filtered = df[
    (df["Pollutant"] == selected_pollutant) &
    (df["Location"].isin(selected_locations))
].copy()

if len(date_range) == 2:
    start_date, end_date = date_range

    filtered = filtered[
        (filtered["Date"].dt.date >= start_date) &
        (filtered["Date"].dt.date <= end_date)
    ]

    period_data = df[
        (df["Location"].isin(selected_locations)) &
        (df["Date"].dt.date >= start_date) &
        (df["Date"].dt.date <= end_date)
    ].copy()
else:
    period_data = df[
        df["Location"].isin(selected_locations)
    ].copy()

# ---------------------------------
# KPI CARDS
# ---------------------------------

st.subheader("Air Quality Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Readings",
    f"{len(filtered):,}"
)

col2.metric(
    "Monitoring Locations",
    filtered["Location"].nunique()
)

col3.metric(
    "Average Concentration",
    f"{filtered['Value'].mean():.2f}"
    if not filtered.empty else "N/A"
)

col4.metric(
    "Selected Pollutant",
    selected_pollutant.upper()
)

st.markdown("---")

# ---------------------------------
# MONTHLY TREND
# ---------------------------------

st.subheader("📈 Monthly Pollution Trend")

if not filtered.empty:

    monthly = (
        filtered.groupby(
            filtered["Date"].dt.to_period("M")
        )["Value"]
        .mean()
        .reset_index()
    )

    monthly["Month"] = monthly["Date"].astype(str)

    fig1 = px.line(
        monthly,
        x="Month",
        y="Value",
        markers=True,
        title=f"Monthly Average {selected_pollutant.upper()}",
        labels={
            "Value": "Average Concentration",
            "Month": "Month"
        }
    )

    st.plotly_chart(fig1, use_container_width=True)

else:
    st.warning("No data available for selected filters.")

# ---------------------------------
# LOCATION COMPARISON
# ---------------------------------

st.subheader("📊 Location-wise Pollution Comparison")

if not filtered.empty:

    location_data = (
        filtered.groupby("Location")["Value"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig2 = px.bar(
        location_data,
        x="Value",
        y="Location",
        orientation="h",
        title="Top 10 Monitoring Locations",
        labels={
            "Value": "Average Concentration",
            "Location": "Monitoring Location"
        }
    )

    fig2.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------
# POLLUTANT DISTRIBUTION
# ---------------------------------

st.subheader("🧪 Pollutant Distribution")

pollutant_data = (
    period_data.groupby("Pollutant")
    .size()
    .reset_index(name="Readings")
)

fig3 = px.pie(
    pollutant_data,
    names="Pollutant",
    values="Readings",
    title="Distribution of Pollution Measurements",
    hole=0.4
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------
# CORRELATION HEATMAP
# ---------------------------------

st.subheader("🔥 Pollutant Correlation Heatmap")

if not period_data.empty:

    pivot = period_data.pivot_table(
        index=["Date", "Location"],
        columns="Pollutant",
        values="Value",
        aggfunc="mean"
    )

    correlation = pivot.corr(min_periods=3)

    if correlation.shape[0] >= 2:
        fig4 = px.imshow(
            correlation,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            title="Correlation Between Pollutants"
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )
    else:
        st.info("Not enough overlapping pollutant data for correlation.")

# ---------------------------------
# DATA TABLE
# ---------------------------------

st.subheader("📋 Air Quality Records")

st.dataframe(
    filtered.sort_values("Date", ascending=False),
    use_container_width=True
)

# ---------------------------------
# DOWNLOAD DATA
# ---------------------------------

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="Filtered_AirQuality.csv",
    mime="text/csv"
)

st.markdown("---")

st.caption(
    "Air Quality Analysis Project | Python | Pandas | Streamlit | Plotly"
)
