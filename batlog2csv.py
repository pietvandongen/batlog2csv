import datetime
import sys

INPUT_KEY_DELIMITER = '"'
INPUT_VALUE_DELIMITER = '" = '
OUTPUT_VALUE_DELIMITER = ','

DATE_KEY = "Date"
CYCLE_COUNT_KEY = "CycleCount"
MAXIMUM_CAPACITY_KEY = "MaxCapacity"
CURRENT_CAPACITY_KEY = "CurrentCapacity"
DESIGN_CAPACITY_KEY = "DesignCapacity"
EXTERNAL_CONNECTED_KEY = "ExternalConnected"

DESIRED_COLUMNS = [
    DATE_KEY,
    CYCLE_COUNT_KEY,
    MAXIMUM_CAPACITY_KEY,
    CURRENT_CAPACITY_KEY,
    DESIGN_CAPACITY_KEY,
    EXTERNAL_CONNECTED_KEY
]


def parsedate(string):
    value = None
    key = None
    isDate = False

    # For dates like "Mon Sep 12 13:29:00 CDT 2013"
    try:
        value = datetime.datetime.strptime(
            string[:20] + string[23:],
            "%a %b %d %H:%M:%S %Y"
        )
    except:
        pass

    # For dates like "Fri 16 Aug 2013 21:47:02 BST"
    try:
        value = datetime.datetime.strptime(
            string[:24],
            "%a %d %b %Y %H:%M:%S"
        )
    except:
        pass

    # For dates like "2013-11-05 18:11:00"
    try:
        value = datetime.datetime.strptime(
            string[:24],
            "%Y-%m-%d %H:%M:%S"
        )
    except:
        pass

    if value:
        key = DATE_KEY
        isDate = True

    return value, key, isDate


# Get the input file name from the provided arguments
try:
    inputFileName = str(sys.argv[1])
except IndexError:
    print "Error: please provide an input file name"
    sys.exit(2)

# Read the input file
try:
    inputFile = open(inputFileName, "r")
    dataLines = inputFile.read().splitlines()
    inputFile.close()
except IOError:
    print "The input file does not exist"
    sys.exit(2)

# Parse the input data
rowCount = 0
columnCount = 0
header = []
row = []
numberOfColumns = 0

for lineNumber, line in enumerate(dataLines):
    value = None
    isDate = False

    # Get the key
    key = line[line.find(INPUT_KEY_DELIMITER) + len(INPUT_KEY_DELIMITER):line.find(INPUT_VALUE_DELIMITER)]

    # Add the value if key column name
    if key in DESIRED_COLUMNS:
        value = line[line.find(INPUT_VALUE_DELIMITER) + len(INPUT_VALUE_DELIMITER):]

    # Try to get a date if key is no column name
    else:
        value, key, isDate = parsedate(line)

    # Add value to row
    if value:
        # New row
        if isDate and row:
            # Print header
            if rowCount == 0:
                numberOfColumns = len(header)
                print OUTPUT_VALUE_DELIMITER.join(header)

            # Print row if it has the correct number of columns
            if len(row) == numberOfColumns:
                print OUTPUT_VALUE_DELIMITER.join(row)

            # Start a new row
            row = []
            rowCount += 1
            columnCount = 0

        # Append column name to header
        if rowCount == 0:
            header.append(key)

        # Convert value
        if key == EXTERNAL_CONNECTED_KEY:
            if value == "Yes":
                value = "true"
            else:
                value = "false"

        # Append value to row
        if columnCount < len(header) and key == header[columnCount]:
            row.append(str(value))

        columnCount += 1

# Print the last row
if len(row) == numberOfColumns:
    print OUTPUT_VALUE_DELIMITER.join(row)
