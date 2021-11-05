# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv
#
# # trying to print a single columns of temperatures
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# Get data in columns
average = sum(temp_list) / len(temp_list)
print(average)
print(data["temp"].mean()) # same result but with less code
print(data["temp"].max())

print(data["condition"])
print(data.condition) # works as the same as previous line


# Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()]) # print day with max temperature

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)
