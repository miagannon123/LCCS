import csv
import pandas as pd  # Import Pandas as pd
import statistics
import matplotlib.pyplot as plt

# Provided data
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
yes_count = 0
no_count = 0
empty_count = 0

for row in data:
    response = row[3]
    if response == "Yes":
        yes_count += 1
    elif response == "No":
        no_count += 1
    elif response == "":
        empty_count += 1

# Pie chart data
labels = ['Yes', 'No', '']
sizes = [yes_count, no_count, empty_count]  # Counts
colors = ['green', 'red', 'gray']
explode = (0, 0, 0.1)  # Explode the empty slice

# Plot
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Responses Distribution')
plt.show()