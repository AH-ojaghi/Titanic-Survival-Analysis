# Titanic Survival Analysis

![Titanic](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/1200px-RMS_Titanic_3.jpg)

## Overview
This project analyzes the Titanic dataset to understand the factors that influenced passenger survival. The dataset contains information about 891 passengers, including their age, gender, passenger class, fare, and more. The goal is to explore the data, clean it, and visualize key insights to identify patterns related to survival.

## Dataset
The dataset is sourced from [Kaggle](https://www.kaggle.com/c/titanic/data) and contains the following columns:
- **PassengerId**: Unique ID for each passenger.
- **Survived**: Survival status (0 = No, 1 = Yes).
- **Pclass**: Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd).
- **Name**: Passenger's name.
- **Sex**: Gender of the passenger.
- **Age**: Age of the passenger.
- **SibSp**: Number of siblings/spouses aboard.
- **Parch**: Number of parents/children aboard.
- **Ticket**: Ticket number.
- **Fare**: Fare paid for the ticket.
- **Cabin**: Cabin number.
- **Embarked**: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

## Analysis Steps
1. **Data Loading and Exploration**:
   - Load the dataset and inspect its structure.
   - Check for missing values and summary statistics.

2. **Data Cleaning**:
   - Handle missing values in `Age`, `Embarked`, and `Cabin`.
   - Drop irrelevant columns.

3. **Data Visualization**:
   - Visualize survival rates by gender, passenger class, and other factors.
   - Analyze age and fare distributions.
   - Explore correlations between numeric features.

4. **Key Insights**:
   - Survival rates were higher for females and passengers in higher classes.
   - Younger passengers and those with larger families had better survival chances.
   - Fare and passenger class were strongly correlated with survival.

## Tools and Libraries
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib

## How to Run the Code
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/titanic-survival-analysis.git