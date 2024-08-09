import pandas as pd

# Example dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, None, 22, None],
    'Salary': [50000, 54000, 58000, None, 62000],
    'Department': ['HR', 'Finance', None, 'Marketing', 'Finance']
}

df = pd.DataFrame(data)
print(df)
print('--------------------1------------------------')
# 1. Drop the records with no value fields
print(df.dropna())

print('--------------------2------------------------')
# 2. Fill the missing fileds with a consatnt value
print(df.fillna(0))
print('--------------------3------------------------')
# 3. Fill mean, median and mode for numerical data
df_filled_mean = df.copy()
df_filled_mean['Age'].fillna(df['Age'].mean(), inplace=True)
df_filled_mean['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df_filled_mean)
print('-------------------4-------------------------')
# 4. Fill with the most frequent value (for categorical data)
df_filled_mode = df.copy()
df_filled_mode['Department'].fillna(df['Department'].mode()[0], inplace=True)
print(df_filled_mode)