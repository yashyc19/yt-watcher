# using numpy and pandas do a dummy analysis of the data
# 1. create a dataframe with the dummy data
# 2. print the first 5 rows of the dataframe
# 3. print the shape of the dataframe
# 4. print the columns of the dataframe
# 5. print the data types of the columns
# 6. print the summary statistics of the dataframe

# import the libraries
import numpy as np
import pandas as pd

def data_analysis(df):
    
    # print the first 5 rows of the dataframe
    print(df.head())
    print('---------------------------------')

    # print the shape of the dataframe
    print(df.shape)
    print('---------------------------------')

    # print the columns of the dataframe
    print(df.columns)
    print('---------------------------------')

    # print the data types of the columns
    print(df.dtypes)
    print('---------------------------------')

    # print the summary statistics of the dataframe
    print(df.describe())
    print('---------------------------------')



def main():    

    # create a dataframe with the dummy data
    data = {
        'name': ['John', 'Jane', 'Doe', 'Alice', 'Bob'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'country': ['USA', 'USA', 'USA', 'USA', 'USA'],
        'company': ['Google', 'Facebook', 'Amazon', 'Microsoft', 'Apple']
    }

    df = pd.DataFrame(data)
    data_analysis(df)

if __name__ == '__main__':
    main()