import streamlit as st
import pandas as pd
import plotly.express as px

from main import PersonGenerator, value_mapper

def get_persons(rows, dist_gender, dist_age, dist_health):
    pg = PersonGenerator(anonymize=False)
    # TODO should refactor class method
    person_list = [pg.generate_person(dist_gender, dist_age, dist_health) for _ in range(rows)]
    df = value_mapper(person_list)
    return df

st.sidebar.subheader("Gender Distribution")
dist_gender_female_male = st.sidebar.slider("Female/Male", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
dist_gender_nb = st.sidebar.slider("Non-Binary", min_value=0.0, max_value=1.0, value=0.02, step=0.01)

# Wonky separation
dist_gender_female = dist_gender_female_male
dist_gender_male = 1 - dist_gender_female_male

st.sidebar.subheader("Age Distribution")
dist_age_mean = st.sidebar.slider("Mean Age", min_value=0, max_value=100, value=42)
dist_age_std = st.sidebar.slider("Age Standard Deviation", min_value=0, max_value=50, value=10)
dist_age_lower_lim = st.sidebar.slider("Lower Age Limit", min_value=0, max_value=100, value=18)
dist_age_upper_lim = st.sidebar.slider("Upper Age Limit", min_value=0, max_value=200, value=80)

st.sidebar.subheader("Health Distribution")
dist_health_mean = st.sidebar.slider("Mean Health", min_value=1, max_value=5, value=3)
dist_health_std = st.sidebar.slider("Health Standard Deviation", min_value=0, max_value=5, value=1)
dist_health_skewness = st.sidebar.slider("Health Skewness", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)

rows = st.slider("Number of Rows", min_value=1, max_value=10_000, value=100)

df = get_persons(
    rows,
    dist_gender={'female': dist_gender_female, 'male': dist_gender_male, 'nb': dist_gender_nb},
    dist_age={'mean': dist_age_mean, 'std': dist_age_std, 'lower_lim': dist_age_lower_lim, 'upper_lim': dist_age_upper_lim},
    dist_health={'mean': dist_health_mean, 'std': dist_health_std, 'skewness': dist_health_skewness}
)

st.dataframe(df)