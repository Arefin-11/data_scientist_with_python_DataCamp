# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():
    cars.loc[lab,"COUNTRY"]=row['country'].upper()


# Print cars
print(cars)

# Use .apply(str.upper) to add COUNTRY column
for lab, row in cars.iterrows() :
    cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)
