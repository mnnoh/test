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
st.title("Risk Perception by Gender")
st.write("Box plots of risk perception scores by gender for various safety areas.")

# Plot boxplots for each category by gender
fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 15))
axes = axes.flatten()

for i, category in enumerate(categories):
    ax = axes[i]
    ax.boxplot([data[data['Gender'] == 'Male'][category].dropna(),
                data[data['Gender'] == 'Female'][category].dropna()],
               labels=['Male', 'Female'])
    ax.set_title(f"{category} Risk Perception")
    ax.set_ylabel("Safety Perception Score (1 = Not Safe, 5 = Very Safe)")

# Hide any unused subplots if categories < 12
for j in range(len(categories), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
st.pyplot(fig)
