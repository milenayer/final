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





