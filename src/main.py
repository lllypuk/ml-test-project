import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('titanic.csv')
    # print(df)
    # print(df.dtypes)
    # print(df.describe().iloc[:, :2])
    # print(df.shape)
    # print(df.isnull().sum())
    # print(df.isnull().mean())
    # print(df.isnull().sum(axis=1).loc[:10])
    # mask = df.isnull().any(axis=1)
    # print(mask.head())
    # print(df[mask].body.head())
    print(df.sex.value_counts(dropna=False))
    print(df.embarked.value_counts(dropna=True))
