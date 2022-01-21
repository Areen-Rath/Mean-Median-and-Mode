import csv

with open("SOCR-HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

length = len(new_data)
new_data.sort()

if length % 2 == 0:
    median1 = float(new_data[length//2])
    median2 = float(new_data[length//2 - 1])
    median = (median1 + median2)/2
else:
    median = new_data[length//2]

print(f"Median is {median}")