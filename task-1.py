file = open("2020-2021.csv", "r")
name_info = {}
next(file)
for line in file:
    splited_line = line.split(",")
    name_info[splited_line[3]] = splited_line[7]
file.close()
name_points = {}
for key, value in name_info.items():
    name_points[key] = 0
    if value == "A":
        name_points[key] += 3
    elif value == "H":
        name_points[key] += 1

place = 0
for key, value in name_points.items():
    place +=1
    print(f"Place: {place}, name: {key}, points: {value}")

file = open("2020-2021.csv", "r")
next(file)
name_goals = {}
for line in file:
    splited_line2 = line.split(",")
    name_goals[splited_line2[3]] = [int(splited_line2[5]) + int(splited_line2[8]), int(splited_line2[6]) + int(splited_line2[9])]

for key, value in name_goals.items():
    print(f"{key} made {value[0]} and missed {value[1]} goals")








