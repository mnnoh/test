import streamlit as st
import pandas as pd
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

# Step 1: Show overall risk perception as a bar chart with colors
st.header("Overall Risk Perception Across All Categories")

# Calculate the mean score for each category
category_means = data[categories].mean()

# Define colors for each risk category
colors = [
    '#1f77b4',  # NaturalDisasters
    '#ff7f0e',  # CollapseExplosion
    '#2ca02c',  # TrafficAccidents
    '#d62728',  # Fire
    '#9467bd',  # FoodSafety
    '#8c564b',  # FoodSecurity
    '#e377c2',  # InfoSecurity
    '#7f7f7f',  # NewDiseases
    '#bcbd22',  # Crime
    '#17becf',  # NuclearRadiation
]

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(categories, category_means, color=colors, edgecolor='black')
ax.set_title("Overall Risk Perception for All Categories")
ax.set_ylabel("Average Safety Perception Score (1 = Not Safe, 5 = Very Safe)")
ax.set_xticklabels(categories, rotation=45, ha='right')  # Rotate labels for readability
st.pyplot(fig)

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
