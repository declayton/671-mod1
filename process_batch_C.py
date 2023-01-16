"""
Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.

"""

import csv

input_file_name = "batchfile_2_kelvin.csv"
output_file_name = "batchfile_3_farenheit.csv"

input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w", newline='')

reader = csv.reader(input_file, delimiter=",")
writer = csv.writer(output_file, delimiter=",")

header = next(reader)
header_list = ["Year","Month","Day","Time","TempF"]
writer.writerow(header_list)

for row in reader:
    Year, Month, Day, Time, TempK = row
    TempF = round((float(TempK) - 273.15) * 9/5 + 32, 2)
    writer.writerow([Year, Month, Day, Time, TempF])

output_file.close()
input_file.close()
