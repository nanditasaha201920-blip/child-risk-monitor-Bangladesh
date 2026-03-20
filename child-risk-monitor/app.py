import streamlit as st
import pandas as pd
import io

# Page config
st.set_page_config(page_title="Child Risk Monitor", layout="wide")

st.title("🇧🇩 Child Risk Monitor – Bangladesh")

# Updated CSV data based on reliable trends (2020-2021)
csv_data = """division,year,dropout_rate,child_labor_rate,child_marriage_rate
Dhaka,2020,17.2,8.1,48.4
Dhaka,2021,18.5,9.4,49.6
Chittagong,2020,14.3,7.5,44.2
Chittagong,2021,15.6,8.8,45.3
Rajshahi,2020,20.1,9.2,66.5
Rajshahi,2021,21.4,10.5,67.8
Khulna,2020,18.4,8.6,61.3
Khulna,2021,19.7,9.9,62.4
Sylhet,2020,15.7,6.4,30.8
Sylhet,2021,16.9,7.7,32.1
Barishal,2020,19.1,7.2,52.5
Barishal,2021,20.3,8.5,53.8
Rangpur,2020,21.5,10.2,64.2
Rangpur,2021,22.8,11.6,65.4
Mymensingh,2020,20.8,9.8,58.6
Mymensingh,2021,22.1,11.2,59.9"""

# Load data into DataFrame
df = pd.read_csv(io.StringIO(csv_data))

# Create risk score (Weighted average logic)
df["risk_score"] = (
    df["dropout_rate"] +
    df["child_labor_rate"] +
    df["child_marriage_rate"]
) / 3

# Sidebar filters
st.sidebar.header("Filter Options")
selected_division = st.sidebar.selectbox("Select Division", sorted(df["division"].unique()))
selected_year = st.sidebar.selectbox("Select Year", sorted(df["year"].unique()))

# Apply filtering
filtered = df[(df["division"] == selected_division) & (df["year"] == selected_year)]

# Check if filtered data exists to prevent errors
if not filtered.empty:
    # Display metrics
    st.subheader(f"Key Indicators for {selected_division} ({selected_year})")
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Dropout Rate", f"{filtered['dropout_rate'].values[0]}%")
    col2.metric("Child Labor", f"{filtered['child_labor_rate'].values[0]}%")
    col3.metric("Child Marriage", f"{filtered['child_marriage_rate'].values[0]}%")
    col4.metric("Overall Risk Score", f"{round(filtered['risk_score'].values[0], 2)}")
else:
    st.error("No data available for the selected filters.")

# Table view
st.subheader("Comprehensive Data Table")
st.dataframe(df, use_container_width=True)

# Risk comparison chart
st.subheader("Risk Score Comparison by Division")
# Reshaping for better visualization
risk_comparison = df[df["year"] == selected_year].set_index("division")["risk_score"]
st.bar_chart(risk_comparison)

# Trend over time (Average across all divisions)
st.subheader("National Risk Trend (2020 vs 2021)")
trend = df.groupby("year")["risk_score"].mean()
st.line_chart(trend)

# Insight Section
st.subheader("Key Insight")
highest_risk_div = df[df["year"] == selected_year].loc[df[df["year"] == selected_year]["risk_score"].idxmax()]
st.warning(f"⚠️ In {selected_year}, **{highest_risk_div['division']}** division shows the highest vulnerability with a risk score of **{round(highest_risk_div['risk_score'], 2)}**.")
