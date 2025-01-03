file = open("2020-2021.csv", "r")
name_red = {}
next(file)
for line in file:
    splited_line = line.split(",")
    name_red[splited_line[3]] = splited_line[7]
file.close()