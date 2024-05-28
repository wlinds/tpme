import os, time
import streamlit as st
import pandas as pd
from main import *
from utils.plots import get_scatter

st.set_page_config(page_title=f"TPME {VERSION}", page_icon="👤", layout="wide")

st.sidebar.header(f'👤 This Person Might Exist')
st.sidebar.text(f'TPME {VERSION}')
st.sidebar.header('People Generation')

anonymize_val = st.sidebar.checkbox("Anonymize")

tokenizer_list = ["Default", "Experimental"]
selected_tokenizer = st.sidebar.selectbox("Tokenizer", tokenizer_list)

languages = ["English", "Swedish"]
selected_language = st.sidebar.selectbox("Column language", languages)

rows = st.sidebar.slider("Rows to generate", min_value=1, max_value=1024, value=100)

with st.sidebar.expander("Name Lengths"):
    name_min_len = st.slider("Minimum Name Length", min_value=1, max_value=20, value=0, step=1)
    name_max_len = st.slider("Maximum Name Length", min_value=7, max_value=30, value=20, step=1)

with st.sidebar.expander("Gender Distribution"):
    dist_gender_female_male = st.slider("Female/Male", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    dist_gender_nb = st.slider("Non-Binary", min_value=0.0, max_value=1.0, value=0.02, step=0.01)

    # Wonky separation
    dist_gender_female = dist_gender_female_male
    dist_gender_male = 1 - dist_gender_female_male

with st.sidebar.expander("Age Distribution"):
    dist_age_mean = st.slider("Mean Age", min_value=0, max_value=100, value=42)
    dist_age_std = st.slider("Age Standard Deviation", min_value=0, max_value=50, value=10)
    dist_age_lower_lim = st.slider("Lower Age Limit", min_value=0, max_value=112, value=18)
    dist_age_upper_lim = st.slider("Upper Age Limit", min_value=0, max_value=112, value=60)

with st.sidebar.expander("Health Distribution"):
    dist_health_mean = st.slider("Mean Health", min_value=1, max_value=5, value=3)
    dist_health_std = st.slider("Health Standard Deviation", min_value=0, max_value=5, value=1)
    dist_health_skewness = st.slider("Health Skewness", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)

@st.cache_data
def get_persons(rows, dist_gender, dist_age, dist_health, name_length, selected_language, anonymize, selected_tokenizer):
    pg = PersonGenerator(anonymize=anonymize, name_tokenizer=selected_tokenizer)
    person_list = [pg.generate_person(dist_gender, dist_age, dist_health, name_length) for _ in range(rows)]
    df = value_mapper(person_list, language=selected_language)
      
    return df

df = get_persons(
    rows,
    dist_gender={'female': dist_gender_female, 'male': dist_gender_male, 'nb': dist_gender_nb},
    dist_age={'mean': dist_age_mean, 'std': dist_age_std, 'lower_lim': dist_age_lower_lim, 'upper_lim': dist_age_upper_lim},
    dist_health={'mean': dist_health_mean, 'std': dist_health_std, 'skewness': dist_health_skewness},
    name_length = {'min_len': name_min_len, 'max_len': name_max_len},
    selected_language=selected_language.lower(),
    anonymize = anonymize_val,
    selected_tokenizer = selected_tokenizer
)


selected_cols = st.multiselect(label=" ", label_visibility="hidden", options=df.columns.tolist(), default=df.columns.tolist())
filtered_df = df[selected_cols]
st.dataframe(filtered_df)


with st.expander('Scatter Plot', expanded=True):
    col_plot, col_options = st.columns([5, 1])

    with col_options:
        st.write(f"**Plot Options:**")
        x_var = st.selectbox('X-axis:', options=filtered_df.columns)
        y_var = st.selectbox('Y-axis:', options=filtered_df.columns)
        col_var = st.selectbox('Color variable:', options=filtered_df.columns)
        size_var = st.selectbox('Size variable:', options=filtered_df.select_dtypes(include=['int']).columns)

        opacity_value = st.slider('Opacity:', min_value=0.1, max_value=1.0, value=0.8, step=0.1)

    with col_plot:
        fig = get_scatter(filtered_df, x_var, y_var, col_var, size_var, opacity_value)
        st.plotly_chart(fig, use_container_width=True)


# Sidebar - Export

with st.sidebar:
    st.header("Export Options")
    export_format = st.selectbox("Export Format", ["csv", "json", "excel", "sql"])
    export_path = st.text_input("Export Path", value= os.getcwd()+'/Exports')
    if st.button("Export"):
        export_manager(filtered_df, export_as=export_format, export_path=export_path, verbose=True)
        export_msg = st.success("Export successful! 🚀✨")
        time.sleep(3)
        export_msg.empty()