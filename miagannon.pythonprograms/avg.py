import csv
import pandas as pd
import statistics

################## PANDAS ########################
# open the file and read it all into one variable
# Read the entire CSV file into a pandas DataFrame
# Calculate the Mean of each searate column by referring to the Column Heading
#DOES FILE NEED TO BE OPENED FIRTS???
#csvfile = open("myfile3.csv","r", newline='')
df = pd.read_csv('myfile3.csv')
print(df.to_string())
# Filter out the column, value_eur
temp_values = df['Temp']
mean_value_temp = round(statistics.mean(temp_values), 2)
print("Mean Value Temp:", mean_value_temp)
noise_values = df['Noise']
mean_value_noise = round(statistics.mean(noise_values), 2)
print("Mean Value Noise:", mean_value_noise)