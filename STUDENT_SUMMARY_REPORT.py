import pandas as pd
import random
import csv


"""CREATING RANDOM STUDENTS DATA"""


data = {
    "Name": ["Hari", "Krishna", "Meena", "John", "Ravi", "Sita", "Anil", "Priya", "Karan", "Divya", 
                   "Amit", "Sneha", "Raj", "Neha", "Vijay", "Rohan", "Pooja", "Deepak", "Gauri", "Suresh",
                   "Reena", "Manoj", "Nisha", "Kiran", "Arjun", "Tina", "Vikas", "Anita", "Rahul", "Lakshmi",
                   "Shyam", "Preeti", "Gopal", "Suman", "Ramesh", "Sunita", "Ajay", "Geeta", "Mohan", "Lata",
                   "Kavita", "Dinesh", "Payal", "Naveen", "Bhavna", "Alok", "Kritika", "Sanjay", "Nitin", "Swati"],
    "Roll No": [i for i in range(101,151)],
    "Marks": [random.randint(35, 100) for _ in range(50)]
}

d1=pd.DataFrame(data)
d1.to_csv("students.csv", mode='a',header=True,index=False)


"""CREATING CODE TO READ CSV FILE"""

df=pd.read_csv("students.csv")

print(df)



total=sum(df["Marks"])
print(total)
avg=total/len(df)
max_marks=max(df["Marks"])
toppers = df[df["Marks"] == max_marks]["Name"].tolist()

print("----- Summary Report -----")
print(f"Total Students: {len(df)}")
print(f"Average Marks: {avg:.2f}")
print(f"Highest Marks: {max_marks}")
print(f"Topper(s): {', '.join(toppers)}")


"""EXPORTING STUDENT SUMMARY TO NEW CSV FILE"""

summary_data = {
    "Total Students": [len(df)],
    "Average Marks": [avg],
    "Highest Marks": [max_marks],
    "Topper(s)": [", ".join(toppers)]
}

summary_df = pd.DataFrame(summary_data)
summary_df.to_csv("student_summary.csv", index=False)

df1=pd.read_csv("student_summary.csv")

print(df1)
