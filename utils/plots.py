import seaborn as sns
import matplotlib.pyplot as plt

def get_histogram(df, title, xlabel, ylabel, bins):
    plt.figure(figsize=(10, 6))
    sns.histplot(df, bins=bins, kde=True, color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()