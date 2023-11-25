# This is a sample Python script.
from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def read_csv():
    csv = 'Source/goodreads_library_export (1).csv'
    df = pd.read_csv(csv)
    print(df.head())
    print(df.info())
    print(df.describe())
    fig, ax = plt.subplots()
    ratings = df['My Rating'].tolist()
    read = df['Exclusive Shelf'].tolist()
    ratings_count = Counter(ratings)
    read_count = Counter(read)
    dict = {}
    for key in ratings:
        for value in read:
            dict[key] = value

    print(dict)
    print(ratings_count)
    print(read_count)
    print(ratings)
    ax.bar(ratings, ratings_count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv()
