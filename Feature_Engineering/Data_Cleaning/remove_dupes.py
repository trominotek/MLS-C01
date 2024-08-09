import pandas as pd

# Example dataset with duplicate rows
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice', 'Bob'],
    'Age': [25, 30, 22, 22, 25, 30],
    'Salary': [50000, 54000, 58000, 58000, 50000, 54000],
    'Department': ['HR', 'Finance', 'Marketing', 'Marketing', 'HR', 'Finance']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print('---------------------------------------')
no_duplicates = df.drop_duplicates()
print(no_duplicates)