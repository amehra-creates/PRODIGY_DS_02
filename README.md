# PRODIGY_DS_02

## 📌 Task 2: Data Cleaning & Exploratory Data Analysis (EDA)

### 🔎 Problem Statement
Perform data cleaning and exploratory data analysis (EDA) on a dataset of your choice, such as the Titanic dataset from Kaggle. Explore the relationships between variables and identify patterns and trends in the data.

---

### 🖥️ Dataset
- **Titanic dataset** (loaded via Seaborn library)
- Contains passenger details such as age, sex, class, fare, survival status, etc.

---

### 🧹 Data Cleaning
- Handled missing values:
  - Filled missing ages with the average age.
  - Dropped rows with missing embarkation values.
- Ensured dataset was consistent and ready for analysis.

---

### 📊 Exploratory Data Analysis (EDA)
Visualizations performed:
1. **Survival Count** → Shows how many passengers survived vs. did not survive.
2. **Survival by Gender** → Compares survival rates between males and females.
3. **Age Distribution** → Histogram showing passenger age spread.
4. **Correlation Heatmap** → Relationships between numeric variables (survival, class, age, fare, family size).

---

### 📈 Key Insights
- More passengers **died (~500)** than survived (~340).
- **Women had higher survival rates** compared to men.
- Most passengers were **young adults (20–30 years old)**.
- **Passenger class strongly influenced survival chances** — higher class passengers had better survival rates.
- Strong negative correlation between **class and fare**, and positive correlation between **family-related variables (sibsp & parch)**.

---

### ⚙️ Technologies Used
- **Python**
- **Pandas** → Data cleaning
- **Seaborn & Matplotlib** → Visualizations

---

### 📂 Files in Repo
- `task2_eda.py` → Python code for cleaning and EDA
- `README.md` → Explanation of the task and findings

---

### 🎯 Outcome
This task demonstrates how data cleaning ensures reliability, and how EDA helps uncover meaningful patterns and relationships in data before building predictive models.
