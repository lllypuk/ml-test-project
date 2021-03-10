import pandas as pd


def read_and_print_file(uri):
    data_frame = pd.read_csv(uri)
    print(data_frame)
    return data_frame


if __name__ == '__main__':
    df = read_and_print_file('titanic.csv')
    print(df.dtypes)
    print(df.describe().iloc[:, :2])
    print(df.shape)
    print(df.isnull().sum())
    print(df.isnull().mean())
    print(df.isnull().sum(axis=1).loc[:10])

