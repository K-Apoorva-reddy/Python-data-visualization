import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("data/employees.csv")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Statistics
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())

# Bar Chart

plt.bar(df["Name"], df["Salary"])
plt.title("Employee Salaries")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.show()


# Pie Chart

department_count = df["Department"].value_counts()

plt.pie(
    department_count,
    labels=department_count.index,
    autopct="%1.1f%%"
)
plt.title("Department Distribution")
plt.show()


# Histogram

plt.hist(df["Salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

#Save cleaned data

df.to_csv("data/cleaned_data.csv", index=False)

print("Cleaned data saved successfully as data/cleaned_data.csv")

print("Project Completed Successfully!")
