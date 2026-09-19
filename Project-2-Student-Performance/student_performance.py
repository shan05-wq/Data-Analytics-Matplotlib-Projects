# Student Performance Analysis

import matplotlib.pyplot as plt

# Data

students = [
    "Ali", "Ahmed", "Sara", "Ayesha", "Hassan",
    "Fatima", "Usman", "Zain", "Hina", "Bilal"
]

math_marks = [
    85, 72, 90, 78, 65,
    88, 70, 95, 82, 75
]

english_marks = [
    78, 68, 85, 80, 60,
    82, 65, 92, 76, 70
]

computer_marks = [
    92, 75, 88, 85, 70,
    95, 72, 98, 90, 78
]

# Calculate Overall Marks

overall_marks = []
for i in range(len(students)):
    avg = (math_marks[i]+english_marks[i]+computer_marks[i])/3

    overall_marks.append(avg)

A = 0
B = 0
C = 0
D = 0

for mark in overall_marks:
    if mark >= 80:
        A += 1
    elif mark >= 70:
        B += 1
    elif mark >=60:
        C += 1
    else:
        D += 1

grades = ["A","B","C","D"]
grades_counts = [A,B,C,D]

fig, ax = plt.subplots(
    2,
    2,
    figsize=(10,6)
)

# Plot1:Subject Average

subjects = ["Math","English","Computer"]
subject_avg = [ sum(math_marks)/len(math_marks),sum(english_marks)/len(english_marks),sum(computer_marks)/len(computer_marks) ]

ax[0,0].bar(subjects,subject_avg)

ax[0,0].set_title("Average marks by Subjects")
ax[0,0].set_xlabel("subject")
ax[0,0].set_ylabel("average marks")

ax[0,0].grid(axis='y',alpha=0.7)

# Plot2:Marks Distrbution

ax[0,1].hist(overall_marks,bins=5,edgecolor="black")

ax[0,1].set_title("Overall Marks Distrbution")
ax[0,1].set_xlabel("Overall Marks")
ax[0,1].set_ylabel("Number of Students")

ax[0,1].grid(axis='y',alpha=0.3)

# Plot3:Math vs Computer Marks

ax[1,0].scatter(math_marks,computer_marks,s=80)

ax[1,0].set_title("Math vs Computer Marks")
ax[1,0].set_xlabel("Math Marks")
ax[1,0].set_ylabel("computer Marks")

ax[1,0].grid(True,alpha=0.3)

# Plot4: Grade Distribution

ax[1, 1].pie(
    grades_counts,
    labels=grades,
    autopct="%1.1f%%",
    startangle=90
)
ax[1,1].set_title("Grade Distribution")

# Overall Dashboard Title

fig.suptitle("Student Performance Analysis",fontsize=18)

# Layout

plt.tight_layout()

plt.savefig("Student_Performance_Dashboard.png",dpi=300,bbox_inches="tight")

plt.show()

