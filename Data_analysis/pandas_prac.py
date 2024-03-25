

# import csv 

# with open("weather_data.csv") as f:
#     data = list(csv.reader(f))
#     temperatures = []
#     for row in data[1:]:
#         temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = data['temp'].max()

# monday = data[data.day == "Monday"]
# temp = monday.temp
# converted = (temp * (9/5)) + 32
# print(converted)

# create dataframe

# data_dict = {
#     "students":["kyle","zee","sihle"],
#     "scores": [76,56,65]
# }

# d = pandas.DataFrame(data_dict)
# d.to_csv("new.csv")