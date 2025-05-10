import csv

with open("ball/players_15.csv", "r", encoding="utf-8") as file:
    data = csv.reader(file, delimiter=",")

    data_list = list(data)  # Convert the CSV reader object to a list

    wages = []
    for row in data_list[1:]:  # Skip the header row
        wages.append(int(row[11]))  # Convert wage to float before appending
        wages
    print(wages[0:10])
    print(sum(wages[0:10]))  # Print the sum of first 10 wages
