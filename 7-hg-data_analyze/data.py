import pandas as pd

data = './gapminder/data-raw/01_pop.tsv'


# by default read_csv() will read a comma separated file,
# our gapminder data set is separated by a tab
# we can use the sep parameter and indicate a tab with \t
df = pd.read_csv(data, sep='\t')


# print out the data
# print(df)


# get the number of rows and columns
# print(df.shape)


# get column names
# print(df.columns)


# get the dtype of each column
# print(df.dtypes)

# get more information about our data
# print(df.info())

# show the first 5 observations
# print(df.head())

# just get the country column and save it to its own variable
# country_df = df['country']
# show the first 5 observations
# print(country_df.head())
# show the last 5 observations
# print(country_df.tail())

# Looking at country, continent, and year
# subset = df[['country', 'year', 'pop']]
# print(subset)

country_df = df['country']
print(type(country_df))