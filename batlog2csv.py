import datetime
import sys

DATE_FORMAT = "%a %b %d %H:%M:%S %Y"
DATE_STRING_CUTOFF = 20
DATE_STRING_CONTINUE = 23
INPUT_KEY_DELIMITER = '"'
INPUT_VALUE_DELIMITER = '" = '
OUTPUT_VALUE_DELIMITER = ','

DATE_KEY = "Date"
CYCLE_COUNT_KEY = "CycleCount"
MAXIMUM_CAPACITY_KEY = "MaxCapacity"
CURRENT_CAPACITY_KEY = "CurrentCapacity"
DESIGN_CAPACITY_KEY = "DesignCapacity"

DESIRED_COLUMNS = [
    DATE_KEY,
    CYCLE_COUNT_KEY,
    MAXIMUM_CAPACITY_KEY,
    CURRENT_CAPACITY_KEY,
    DESIGN_CAPACITY_KEY
]

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
header = []
row = []
numberOfColumns = 0

for lineNumber, line in enumerate(dataLines):
    value = None
    date = False

    # Get the key
    key = line[line.find(INPUT_KEY_DELIMITER) + len(INPUT_KEY_DELIMITER):line.find(INPUT_VALUE_DELIMITER)]

    # Add the value if key is desired
    if key in DESIRED_COLUMNS:
        value = line[line.find(INPUT_VALUE_DELIMITER) + len(INPUT_VALUE_DELIMITER):]

    # Try to get a date if key is not desired
    else:
        try:
            value = str(datetime.datetime.strptime(line[:DATE_STRING_CUTOFF] + line[DATE_STRING_CONTINUE:], DATE_FORMAT))
            key = DATE_KEY
            date = True
        except:
            pass

    # Add value to row
    if value:
        # New row
        if date and row:
            # Print header
            if rowCount == 0:
                numberOfColumns = len(row)
                print OUTPUT_VALUE_DELIMITER.join(header)

            # Print row if it has the correct number of columns
            if len(row) == numberOfColumns:
                print OUTPUT_VALUE_DELIMITER.join(row)

            # Start a new row
            row = []
            rowCount += 1

        # Append column name to header
        if rowCount == 0:
            header.append(key)

        # Append value to row
        row.append(value)

# Print the last row
if len(row) == numberOfColumns:
    print OUTPUT_VALUE_DELIMITER.join(row)
