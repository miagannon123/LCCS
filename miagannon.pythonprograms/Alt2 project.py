import csv
import pandas as pd  # Import Pandas as pd
import statistics
import matplotlib.pyplot as plt

csvfile = open("myfile.csv","x")
print("File Created")

csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Date', 'LC regret Y/N', 'What Subject', 'Core Level Regret Y/N', 'What subject and level'])
print("Columns Created")

data = [
    ["19/1/24", "No", "", "No", ""],
    ["19/1/24", "No", "", "Yes", "Higher Maths"],
    ["19/1/24", "No", "", "Yes", "Higher Maths"],
    ["19/1/24", "No", "", "No", ""],
    ["19/1/24", "No", "", "No", ""],
    ["19/1/24", "Yes", "Accounting", "No", ""],
    ["19/1/24", "No", "", "No", ""],
    ["19/1/24", "No", "", "Yes", "Higher Irish"],
    ["19/1/24", "Yes", "Computer Science", "Yes", "Ordinary Irish"],
    ["24/1/19", "Yes", "Computer Science", "No", ""],
    ["19/1/2024", "Yes", "Accounting", "No", ""],
    ["19/1/2024", "No", "", "Yes", "Higher Maths"],
    ["19/1/2024", "Yes", "French", "Yes", "Higher Irish"],
    ["19/1/2024", "Yes", "Computer Science", "Yes", "Ordinary Irish"],
    ["19/1/2024", "No", "", "Yes", "Higher Maths"],
    ["19/1/2024", "Yes", "Politics", "No", ""],
    ["19/1/2024", "Yes", "Computer Science", "Yes", "Higher Maths"],
    ["19/1/2024", "Yes", "Chemistry", "No", ""],
    ["19/1/2024", "No", "", "No", ""],
    ["20/1/2024", "No", "", "Yes", "Higher Irish"],
    ["20/1/2024", "Yes", "Biology", "No", ""],
    ["20/1/2024", "No", "", "No", ""],
    ["22/1/2024", "No", "", "Yes", "Higher Maths"],
    ["23/1/2024", "Yes", "LCVP", "Yes", "Higher English"]
]

# Count occurrences of "Yes", "No", and empty strings in the fourth column
labels = ['yes', 'no']
sizes = [54.16, 45.83]  # Percentages
colors = ['orange', 'green']
explode = (0, 0.1)  # explode 2nd & 4th slice (i.e. 'Snapchat & Tiktok')

# Plot
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Do you 5th Year regret choosing a Lc subject')

labels = ['Accounting', 'Computer Science', 'Politics', 'Chemistry','Biology', 'LCVP', 'French']
sizes = [18.18, 36.36, 9.09, 9.09, 9.09, 9.09, 9.09]  # Percentages
colors = ['pink', 'blue','green','yellow','purple','red','orange']
explode = (0, 0.1, 0, 0, 0, 0, 0)  # explode 2nd slice (Computer Science)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('what subject do 5th years regret')

plt.show()





      

