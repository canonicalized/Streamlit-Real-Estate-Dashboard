import streamlit as st
import pandas as pd

st.set_page_config(page_title="Real Estate App", layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

data = {
    'Location': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Los Angeles', 'Chicago'],
    'Price': [500000, 700000, 650000, 600000, 750000, 600000],
    'Bedrooms': [3, 4, 2, 3, 4, 2],
    'Bathrooms': [2, 2, 1, 2, 2, 1],
    'Size (sqft)': [1200, 1500, 900, 1200, 1500, 900],
    'latitude': [40.730610, 34.052235, 41.878114, 40.730610, 34.052235, 41.878114],
    'longitude': [-73.935242, -118.243683, -87.629798, -73.935242, -118.243683, -87.629798]
}

df = pd.DataFrame(data)

# Create a header
st.header("Real Estate Dashboard")

# Create filters across the top
location_filter = st.sidebar.selectbox("Location", ["All", "New York", "Los Angeles", "Chicago"])
price_filter = st.sidebar.slider("Price Range", min_value=0, max_value=1000000, value=(0, 1000000))

# Create a map on the left and a line chart on the right in the top row
col1, col2 = st.columns(2)
with col1:
    st.map(df[['latitude','longitude']])

with col2:
    st.line_chart(df)

st.dataframe(df)

st.markdown("Bye bye")