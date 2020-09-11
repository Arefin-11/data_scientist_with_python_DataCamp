# Import pandas using the alias pd
import pandas as pd

#homelessness is a DataFrame

#To see the first few rows to get a idea about the data
homelessness.head()

#.info() shows information on each of the columns, such as the data type and number of missing values.
homelessness.info()

#.shape returns the number of rows and columns of the DataFrame.
homelessness.shape

#.describe() calculates a few summary statistics for each column.
homelessness.describe()

# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)
