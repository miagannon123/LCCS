import csv
import pandas
import statistics

tottemp=0
recct=0
# Open the file read it and print the first 2 rows
csvfile = open("myfile3.csv","r", newline='')
csv_reader = csv.reader(csvfile)
header = next(csv_reader, None)

line = csvfile.readline()
print(line)
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)
#print(line, "readline1")

line = csvfile.readline()
print(line)
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)

line = csvfile.readline()
print(line)
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)

line = csvfile.readline()
print(line)
columns=line.strip().split(',')
column1=columns[0]
tottemp=tottemp+int(column1)
recct=recct+1
print("Tottemp",tottemp," ",recct)


df = pandas.read_csv('myfile3.csv')
print(df.to_string())
# Filter out the column, value_eur
temp_values = df['Temp']
mean_value_temp = round(statistics.mean(temp_values), 2)
print("Mean Value Temp:", mean_value_temp)
noise_values = df['Noise']
mean_value_noise = round(statistics.mean(noise_values), 2)
print("Mean Value Noise:", mean_value_noise)