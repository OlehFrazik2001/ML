import pandas as pd
import pandas as pn
import matplotlib.pyplot as plt

def trans(x):
    x = str(x).split('-')
    return (int(x[0]) + int(x[1]) / 12) * 0.3048


dfNba = pn.read_csv('nba.csv', ',')
dfEmployees = pn.read_csv('employees.csv', ',')
print("Стовпці, які містять порожні дані у \"Employees\"")
print(dfEmployees.columns[dfEmployees.isna().any()])
dfEmployees = dfEmployees.dropna()
print("Стовпці, які містять порожні дані у \"nba\"")
print(dfNba.columns[dfNba.isna().any()])
dfNba = dfNba.dropna()
print("Вага після трансформації")
dfNba['Weight'] = dfNba['Weight'].transform(lambda x: x * 0.45359237)
print("Висота після трансформації")
dfNba['Height'] = dfNba['Height'].transform(trans)
print(dfNba['Height'])
print("Мінімальний зріст у м")
print(dfNba['Height'].min())
print("Максимальна вага у кг")
print(dfNba['Weight'].max())
print("Середня зарплата")
print(dfEmployees['Salary'].mean())
print("Загальна зарплата гравців по командах")
print(dfNba['Salary'].groupby(dfNba['Team']).sum())
print("Роботодавці із значенням \"Senior Management\":\"True\"")
print(dfEmployees[dfEmployees['Senior Management'] == True])

df2 = dfNba[['Salary', 'Team']]
df2 = df2.groupby(dfNba['Team']).mean().reset_index()
plt.xticks(rotation=60)
plt.bar(df2['Team'], df2['Salary'])
plt.show()

df1 = dfEmployees[['Gender', 'Salary']]
df1 = df1.groupby(df1['Gender']).mean().reset_index()
plt.bar(df1['Gender'], df1['Salary'])
plt.show()
dfNba.to_csv('nbaNew.csv')
dfEmployees.to_csv('employeesNew.csv')
