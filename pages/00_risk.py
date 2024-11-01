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

# Step 1: Show overall box plot for all risk categories combined (without gender distinction)
st.header("Overall Risk Perception Across All Categories")
fig, ax = plt.subplots(figsize=(12, 8))
data[categories].boxplot(ax=ax)
ax.set_title("Overall Risk Perception for All Categories")
ax.set_ylabel("Safety Perception Score (1 = Not Safe, 5 = Very Safe)")
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
