"""
Batch Process - third transformation

Reads from a file, transform, write to a new file.

In this case, covert degree K to degree F.

"""

import csv

# Declare a variable to hold the input file name
# Declare a variable to hold the output file name
input_file_name = "batchfile_2_kelvin.csv"
output_file_name = "batchfile_3_farenheit.csv"

# Create a file object for input (r = read access)
# Create a file object for output (w = write access)
# On Windows, without newline='', 
# we'll get an extra line after each record
input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w", newline='')

# Create a csv reader for a comma delimited file
# Create a csv writer for a comma delimited file
reader = csv.reader(input_file, delimiter=",")
writer = csv.writer(output_file, delimiter=",")

# Our file has a header row, move to next to get to data
# Write the header row to the output file
header = next(reader)
header_list = ["Year","Month","Day","Time","TempF"]
writer.writerow(header_list)

# Then, for each data row in the reader
    # set local variables for each column in the row
    # convert the temperature from K to F
    # put the values in a list (see the square brackets) 
    # and write the list of values to the output file
for row in reader:
    Year, Month, Day, Time, TempK = row
    TempF = round((float(TempK) - 273.15) * 9/5 + 32, 2)
    writer.writerow([Year, Month, Day, Time, TempF])

# close the file objects to release the resources
output_file.close()
input_file.close()
