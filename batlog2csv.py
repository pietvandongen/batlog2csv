import sys
from collections import OrderedDict
import datetime

DATE_FORMAT = "%a %b %d %H:%M:%S %Y"
DATE_STRING_CUTOFF = 20
DATE_STRING_CONTINUE = 23
INPUT_VALUE_DELIMITER = '" = '
OUTPUT_VALUE_DELIMITER = ','
SEGMENT_START = 1
SEGMENT_END = 8

DATE = "Date"
DESIGN_CYCLE_COUNT_70 = "DesignCycleCount70"
CYCLE_COUNT = "CycleCount"
DESIGN_CYCLE_COUNT_9C = "DesignCycleCount9C"
MAXIMUM_CAPACITY = "MaxCapacity"
CURRENT_CAPACITY = "CurrentCapacity"
DESIGN_CAPACITY = "DesignCapacity"

SEGMENTS = OrderedDict([
    (DATE, 1),
    (DESIGN_CYCLE_COUNT_70, 2),
    (CYCLE_COUNT, 3),
    (DESIGN_CYCLE_COUNT_9C, 4),
    (MAXIMUM_CAPACITY, 5),
    (CURRENT_CAPACITY, 6),
    (DESIGN_CAPACITY, 8)
])

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

# Print the header
print(OUTPUT_VALUE_DELIMITER.join(SEGMENTS))

# Parse the input data
# It expects sections of 8 lines, starting with a data, followed by seven key / pair values, each on a new line
segmentLineCount = 1

for lineNumber, line in enumerate(dataLines):
    if segmentLineCount == SEGMENT_START:
        row = []

    if segmentLineCount == SEGMENTS[DATE]:
        try:
            row.append(str(
                datetime.datetime.strptime(line[:DATE_STRING_CUTOFF] + line[DATE_STRING_CONTINUE:], DATE_FORMAT)
            ))
        except ValueError, e:
            print("Could not parse date from string '" + line + "' on line " + str(lineNumber + 1))
            print("Cause: " + e.message)
            sys.exit(2)

    elif segmentLineCount == SEGMENTS[DESIGN_CYCLE_COUNT_70]:
        try:
            row.append(str(int(line[line.find(INPUT_VALUE_DELIMITER) + len(INPUT_VALUE_DELIMITER):])))
        except ValueError:
            segmentLineCount = SEGMENT_START

    elif segmentLineCount == SEGMENTS[CYCLE_COUNT]:
        try:
            row.append(str(int(line[line.find(INPUT_VALUE_DELIMITER) + len(INPUT_VALUE_DELIMITER):])))
        except ValueError:
            segmentLineCount = SEGMENT_START

    elif segmentLineCount == SEGMENTS[DESIGN_CYCLE_COUNT_9C]:
        try:
            row.append(str(int(line[line.find(INPUT_VALUE_DELIMITER) + len(INPUT_VALUE_DELIMITER):])))
        except ValueError:
            segmentLineCount = SEGMENT_START

    elif segmentLineCount == SEGMENTS[MAXIMUM_CAPACITY]:
        try:
            row.append(str(int(line[line.find(INPUT_VALUE_DELIMITER) + len(INPUT_VALUE_DELIMITER):])))
        except ValueError:
            segmentLineCount = SEGMENT_START

    elif segmentLineCount == SEGMENTS[CURRENT_CAPACITY]:
        try:
            row.append(str(int(line[line.find(INPUT_VALUE_DELIMITER) + len(INPUT_VALUE_DELIMITER):])))
        except ValueError:
            segmentLineCount = SEGMENT_START

    elif segmentLineCount == SEGMENTS[DESIGN_CAPACITY]:
        try:
            row.append(str(int(line[line.find(INPUT_VALUE_DELIMITER) + len(INPUT_VALUE_DELIMITER):])))
        except ValueError:
            segmentLineCount = SEGMENT_START

    if segmentLineCount == SEGMENT_END:
        print(OUTPUT_VALUE_DELIMITER.join(row))
        segmentLineCount = SEGMENT_START
    else:
        segmentLineCount += SEGMENT_START
