# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
data = pd.read_csv(url)

# Display basic information about the dataset
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset information:")
print(data.info())

print("\nSummary statistics:")
print(data.describe())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Data Cleaning
# Fill missing 'Age' with the median value
data['Age'] = data['Age'].fillna(data['Age'].median())

# Fill missing 'Embarked' with the most common value
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])

# Drop the 'Cabin' column as it has too many missing values
data = data.drop('Cabin', axis=1)

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(data.isnull().sum())

# Data Visualization
# 1. Survival Count
plt.figure(figsize=(8, 6))
sns.countplot(x='Survived', data=data, hue='Survived', palette='Set2', legend=False)
plt.title('Survival Count (0 = No, 1 = Yes)')
plt.show()

# 2. Survival by Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', hue='Survived', data=data, palette='Set2')
plt.title('Survival by Gender')
plt.show()

# 3. Survival by Passenger Class
plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', hue='Survived', data=data, palette='Set2')
plt.title('Survival by Passenger Class')
plt.show()

# 4. Age Distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['Age'], bins=20, kde=True, color='blue')
plt.title('Age Distribution')
plt.show()

# 5. Fare Distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['Fare'], bins=20, kde=True, color='green')
plt.title('Fare Distribution')
plt.show()

# 6. Correlation Heatmap
plt.figure(figsize=(10, 8))
# Select only numeric columns for correlation
numeric_data = data.select_dtypes(include=[np.number])
corr = numeric_data.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# 7. Survival by Age and Gender
plt.figure(figsize=(10, 6))
sns.violinplot(x='Sex', y='Age', hue='Survived', data=data, split=True, palette='Set2')
plt.title('Survival by Age and Gender')
plt.show()

# 8. Survival by Embarked Port
plt.figure(figsize=(8, 6))
sns.countplot(x='Embarked', hue='Survived', data=data, palette='Set2')
plt.title('Survival by Embarked Port')
plt.show()

# 9. Family Size Analysis
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
plt.figure(figsize=(8, 6))
sns.countplot(x='FamilySize', hue='Survived', data=data, palette='Set2')
plt.title('Survival by Family Size')
plt.show()

# 10. Fare vs. Survival
plt.figure(figsize=(8, 6))
sns.boxplot(x='Survived', y='Fare', data=data, hue='Survived', palette='Set2', legend=False)
plt.title('Fare vs. Survival')
plt.show()