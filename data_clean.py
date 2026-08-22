#importing necessary libraries
import pandas as pd
import numpy as np

#Loading the dataset
df=pd.read_csv(r"C:\Users\ROHIT RAJ\Downloads\indian_employee_data (1) - indian_employee_data (1).csv")
print(df.head())


#Checking the missing values
print('Missing values in each columns')
print(df.isnull().sum())

df['Salary (INR)'].fillna(df['Salary (INR)'].mean(),inplace=True)
df['Performance Rating'].fillna(df['Performance Rating'].median(),inplace=True)


#Replacing infinte val
df.replace([np.inf,-np.inf],np.nan,inplace=True)

df.fillna(df.mean(numeric_only=True),inplace=True)

#Removing duplicates  records
df.drop_duplicates(inplace=True)

#Replacing the negative salaries
df['Salary (INR)']=np.where(df['Salary (INR)']<0,df['Salary (INR)'].mean(),df['Salary (INR)'])

#Handling outliers
salary_mean=df['Salary (INR)'].mean()
salary_std=df['Salary (INR)'].std()
lower_bound=salary_mean-(3*salary_std)
upper_bound=salary_mean+(3*salary_std)


df=df[(df['Salary (INR)']>=lower_bound)& (df['Salary (INR)']<=upper_bound)]

df.to_csv('Cleaned_indian_empolyee_data.csv',index=False)


print('Data cleaning Completed! Saved as Cleaned_indian_empolyee_data')

