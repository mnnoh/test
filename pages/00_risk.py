import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load data
file_path = 'test.csv'
data = pd.read_csv(file_path)

# Rename columns for readability
data.columns = ['ID', 'Gender', 'NaturalDisasters', 'CollapseExplosion', 'TrafficAccidents', 
                'Fire', 'FoodSafety', 'FoodSecurity', 'InfoSecurity', 'NewDiseases', 
                'Crime', 'NuclearRadiation']

# Convert Gender to categorical labels
data['Gender'] = data['Gender'].map({1: 'Male', 2: 'Female'})

# List of categories to visualize
categories = data.columns[2:]

# Streamlit layout
st.title("Risk Perception Analysis")

# Step 1: Show overall risk perception as an interactive bar chart with Plotly
st.header("Overall Risk Perception Across All Categories")

# Calculate the mean score for each category
category_means = data[categories].mean().round(2)  # Round to 2 decimal places for display

# Create a Plotly bar chart with custom hover information
fig = px.bar(
    x=categories, 
    y=category_means, 
    labels={'x': 'Risk Category', 'y': 'Average Safety Perception Score (1 = Not Safe, 5 = Very Safe)'},
    title="Overall Risk Perception for All Categories",
    color=categories, 
    color_discrete_sequence=px.colors.qualitative.Bold,
    hover_data={'y': True}  # Only show the y value (average) on hover
)

# Update hover template to show only the average value
fig.update_traces(hovertemplate='Average Score: %{y}')

# Set y-axis limit to 5
fig.update_layout(yaxis=dict(range=[0, 5]))

# Display Plotly chart
st.plotly_chart(fig)

# Step 2: Select individual risk category for gender-specific box plot
st.header("Gender Comparison for Selected Risk Category")
selected_category = st.selectbox("Select a Risk Category", options=categories)

fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot([data[data['Gender'] == 'Male'][selected_category].dropna(),
            data[data['Gender'] == 'Female'][selected_category].dropna()],
           labels=['Male', 'Female'])
ax.set_title(f"{selected_category} Risk Perception by Gender")
ax.set_ylabel("Safety Perception Score (1 = Not Safe, 5 = Very Safe)")
st.pyplot(fig)
