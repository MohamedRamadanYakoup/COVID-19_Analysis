import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('csse_covid_19_data\csse_covid_19_daily_reports\\03-15-2020.csv')

print(df.head())

