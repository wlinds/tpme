import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def get_histogram(df, title, xlabel, ylabel, bins):
    plt.figure(figsize=(10, 6))
    sns.histplot(df, bins=bins, kde=True, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def get_histogram_subplots(df, title, xlabel, ylabel, bins):
    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    sns.histplot(df[0], bins=bins[0], kde=True, color='skyblue', edgecolor='black')
    plt.title(title[0])
    plt.xlabel(xlabel[0])
    plt.ylabel(ylabel[0])
    plt.grid(True)

    plt.subplot(1, 2, 2)
    sns.histplot(df[1], bins=bins[1], kde=True, color='skyblue', edgecolor='black')
    plt.title(title[1])
    plt.xlabel(xlabel[1])
    plt.ylabel(ylabel[1])
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def get_scatter(df, x_col, y_col, color_col, size_col, opacity_value):
    hover_data = ['Name'] if 'Name' in df.columns else (['Namn'] if 'Namn' in df.columns else None)
    fig = px.scatter(df, x=x_col, y=y_col, color=color_col, size=size_col, opacity=opacity_value,
                     hover_data=hover_data)
    return fig