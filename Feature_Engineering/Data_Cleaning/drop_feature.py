import pandas as pd

# Example dataset with more missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, None, 22, None],
    'Salary': [None, 54000, None, None, None],
    'Department': [None, 'Finance', None, 'Marketing', 'Finance']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print('----------------------------------------')
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)
columns_to_drop = missing_percentage[missing_percentage > 70].index
print(columns_to_drop)
df_dropped = df.drop(columns=columns_to_drop)
print(df_dropped)