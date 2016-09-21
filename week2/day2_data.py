import csv

with open("data.csv") as open_file:
    contents = open_file.readlines()

# print(contents[2].split(",")[2])

# print(contents)
clean_data = [row.replace("\n","").split(",") for row in contents]
# print(clean_data[11][4])
# print(clean_data)

with open("data.csv") as open_file:
    # contents = csv.reader(open_file, delimiter="|")
    contents = csv.DictReader(open_file, delimiter="|")#, fieldnames=["id", "Wave Height", "Wave Period", "Avg Waves Per Second", "Water Temp", "Date"])
    print(list(contents)[1])
