# This is a sample Python script.
from collections import Counter
from datetime import datetime
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
    # print(ratings)
    # ax.bar(ratings, ratings_count)
    # print(df['Author'])
    # authors = df['Author']
    date_str = '01-01-2023'
    compare_date = datetime.strptime(date_str, '%m-%d-%Y').date()
    print(type(compare_date))
    print(compare_date)
    authors = []
    for index, row in df.iterrows():
        # print(row['Date Read'])
        if len(str(row['Date Read'])) > 3:
            # print(row['Date Read'])
            read_date = str(row['Date Read'])
            read_date.replace('/', '-')
            # print(read_date)
            date = datetime.strptime(read_date, '%Y/%m/%d').date()

            if date >= compare_date:
                print(row['Date Read'])
                authors.append(row['Author'])
    authors_df = pd.DataFrame({'author':authors})
    print(authors_df['author'])
    authors_df.to_csv('Source/out.csv')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_csv()
