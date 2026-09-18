import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Titanic dataset (from seaborn for simplicity)
titanic = sns.load_dataset("titanic")

# Step 1: Data Cleaning
print("Missing values before cleaning:")
print(titanic.isnull().sum())

# Fill missing age values with average age
titanic['age'].fillna(titanic['age'].mean(), inplace=True)

# Drop rows where 'embarked' is missing
titanic.dropna(subset=['embarked'], inplace=True)

print("\nMissing values after cleaning:")
print(titanic.isnull().sum())

# Step 2: Exploratory Data Analysis (EDA)

# Survival count
sns.countplot(x="survived", data=titanic)
plt.title("Survival Count")
plt.show()

# Survival by gender
sns.countplot(x="sex", hue="survived", data=titanic)
plt.title("Survival by Gender")
plt.show()

# Age distribution
sns.histplot(titanic['age'], bins=20, kde=True)
plt.title("Age Distribution of Passengers")
plt.show()

# # Correlation heatmap
# sns.heatmap(titanic.corr(), annot=True, cmap="coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()

# Correlation heatmap (only numeric columns)
numeric_data = titanic.select_dtypes(include=['float64','int64'])
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
