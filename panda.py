import pandas as pd
import numpy as np2

#Q5
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

filtered = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print("Filtered:\n", filtered)

print()

#Q6
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

print(df[['Min.Price', 'Max.Price']])

print()

#Q7
df2 = pd.DataFrame(np2.random.randint(10, 50, 25).reshape(5, 5))
over_100_sums = df2[df2.sum(axis=1) > 100]
print("Rows with sum greater than 100:\n", over_100_sums)
