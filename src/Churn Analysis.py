#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load dataset
df = pd.read_csv(r'c:\Users\User\OneDrive\Desktop\Customer Churn.csv')
df.head()
#Initial exploration
print(df.shape)
print(df.dtypes)
print(df.info)
print(df.describe())
#check missing and duplicated values
print(df.isnull().sum())
print(df.duplicated().sum())
#convert total charges into numeric
df["TotalCharges"] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
print(df.dtypes)

# filling missing value of total charges
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
#EDA
#Churn Distribution
plt.figure(figsize=(8,5))
ax = sns.countplot(x='Churn', data=df)
for container in ax.containers:
    ax.bar_label(container)
plt.title("Churn Distribution")
plt.show()

#Gender Distribution
plt.figure(figsize=(8,5))
ax = sns.countplot(x='gender', data=df, hue = 'Churn')
for container in ax.containers:
    ax.bar_label(container)
plt.title("Gender Distribution")
plt.show()

#contract type vs churn
plt.figure(figsize=(8,5))
ax = sns.countplot(x='Contract',data=df, hue="Churn")
for container in ax.containers:
    ax.bar_label(container)
plt.title("Contract Type vs Churn")
plt.show()

#Internet service vs churn
plt.figure(figsize=(8,5))
ax = sns.countplot(x='InternetService', data=df, hue='Churn')
for container in ax.containers:
    ax.bar_label(container)
plt.title("Internet Service vs Churn")
plt.show()

#Payment method vs churn
plt.figure(figsize=(10,5))
ax = sns.countplot(x="PaymentMethod", data=df, hue='Churn')
for container in ax.containers:
    ax.bar_label(container)
plt.title("Payment Method vs Churn")
plt.show()

#Monthly charges distribution
plt.figure(figsize=(8,5))
sns.histplot(x="MonthlyCharges", data=df, kde= True, hue='Churn')
plt.title("Monthly Charges Distribution")
plt.show()

#Tenure Analysis
plt.figure(figsize=(8,5))
sns.boxplot(x='Churn', y = 'tenure', data=df )
plt.title("Tenure Analysis")
plt.show()

#correlation analysis
corr = df.corr(numeric_only = True)
plt.figure(figsize=(8,5))
sns.heatmap(corr,annot=True,cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
#saved cleaned dataset
df.to_csv(r'c:\Users\User\OneDrive\Desktop\Cleaned Customer Churn.csv', index=False)