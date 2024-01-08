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
    sr = pd.Series(df['Author'])
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


    date_str = '01-01-2023'
    compare_date = datetime.strptime(date_str, '%m-%d-%Y').date()
    print(type(compare_date))
    print(compare_date)
    authors = []
    for index, row in df.iterrows():
        print(len(str(row['Date Read'])))
        if len(str(row['Date Read'])) > 3:
            read_date = str(row['Date Read'])
            read_date.replace('/', '-')
            date = datetime.strptime(read_date, '%m/%d/%Y').date()
            if date >= compare_date:
                print(row['Date Read'], row['Title'])
                if row['Author'] not in authors:
                    authors.append(row['Author'])
                    print('count = ' + str(sr.value_counts()[row['Author']]))
    authors_df = pd.DataFrame({'author':authors, 'nationality':'', 'read count':''})
    for index, row in authors_df.iterrows():
        row['read count'] = sr.value_counts()[row['author']]
    print(authors_df['author'])
    authors_df.to_csv('Source/out.csv')

def author_read_count():
    csv = 'Source/authors.csv'
    fig, ax = plt.subplots()
    df = pd.read_csv(csv)
    numbers = []
    authors = []
    for number in df['read count']:
        if number > 1:
            numbers.append(int(number))
    print(numbers)
    for index, row in df.iterrows():
        if int(row['read count']) > 1:
            authors.append(row['author'].split(' ')[1])

    ax.bar(authors, numbers)

    plt.show()


def author_nationality():
    csv = 'Source/authors.csv'
    fig, ax = plt.subplots()
    df = pd.read_csv(csv)
    nations = []
    nations_dict = {}
    for nation in df['nationality']:
        if nation not in nations:
            nations.append(nation)
        if nation not in nations_dict:
            nations_dict[nation] = 0
        if nation in nations_dict:
            nations_dict[nation] += 1

    ax.bar(nations_dict.keys(), nations_dict.values())
    plt.show()

def ratings_count():
    csv = 'Source/goodreads_library_export (1).csv'
    df = pd.read_csv(csv)
    ratings = []
    ratings_dict = {}
    fig, ax = plt.subplots()

    for rating in df['My Rating']:
        if int(rating)> 0:
            ratings.append(int(rating))

            if rating not in ratings_dict:
                ratings_dict[rating] = 0
            if rating in ratings_dict:
                ratings_dict[rating] += 1

    average = sum(ratings) / len(ratings)
    most_common_rating = max(set(ratings), key=ratings.count)
    print(average)
    print(most_common_rating)

    ax.bar(ratings_dict.keys(), ratings_dict.values())

    plt.show()

if __name__ == '__main__':
    # read_csv()
    # author_read_count()
    # author_nationality()
    ratings_count()
