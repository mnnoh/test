import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
st.write("Distribution of risk perception scores by gender for various safety areas.")

# Gender selection
gender = st.selectbox("Select Gender", options=['Male', 'Female'])

# Filter data by selected gender
gender_data = data[data['Gender'] == gender]

# Plot distribution for each category
for category in categories:
    st.subheader(f"{category} Risk Perception")
    fig, ax = plt.subplots()
    sns.histplot(gender_data[category], bins=5, kde=True, ax=ax)
    ax.set_xlabel("Safety Perception Score (1 = Not Safe, 5 = Very Safe)")
    ax.set_ylabel("Frequency")
    ax.set_title(f"{category} Perception for {gender}")
    st.pyplot(fig)
