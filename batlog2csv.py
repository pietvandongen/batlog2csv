import datetime
import sys


class Batlog2Csv:
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

    def __init__(self, data_lines):
        self.dataLines = data_lines

    def convert(self):
        csv = ""
        rowcount = 0
        column_count = 0
        header = []
        row = []
        number_of_columns = 0

        for lineNumber, line in enumerate(self.dataLines):
            value = None
            is_date = False

            # Get the key
            key = line[line.find(self.INPUT_KEY_DELIMITER) + len(self.INPUT_KEY_DELIMITER):line.find(
                self.INPUT_VALUE_DELIMITER)]

            # Add the value if key column name
            if key in self.DESIRED_COLUMNS:
                value = line[line.find(self.INPUT_VALUE_DELIMITER) + len(self.INPUT_VALUE_DELIMITER):]

            # Try to get a date if key is no column name
            else:
                value, key, is_date = self.parse_date(line)

            # Add value to row
            if value:
                # New row
                if is_date and row:
                    # Print header
                    if rowcount == 0:
                        number_of_columns = len(header)
                        csv += self.OUTPUT_VALUE_DELIMITER.join(header) + "\n"

                    # Print row if it has the correct number of columns
                    if len(row) == number_of_columns:
                        csv += self.OUTPUT_VALUE_DELIMITER.join(row) + "\n"

                    # Start a new row
                    row = []
                    rowcount += 1
                    column_count = 0

                # Append column name to header
                if rowcount == 0:
                    header.append(key)

                # Convert value
                if key == self.EXTERNAL_CONNECTED_KEY:
                    if value == "Yes":
                        value = "true"
                    else:
                        value = "false"

                # Append value to row
                if column_count < len(header) and key == header[column_count]:
                    row.append(str(value))

                column_count += 1

        # Add the last row
        if len(row) == number_of_columns:
            csv += self.OUTPUT_VALUE_DELIMITER.join(row) + "\n"

        return csv

    @staticmethod
    def parse_date(string):
        value = None
        key = None
        is_date = False

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
            key = Batlog2Csv.DATE_KEY
            is_date = True

        return value, key, is_date


def main():
    try:
        input_file_name = str(sys.argv[1])
    except IndexError:
        print "Error: please provide an input file name"
        sys.exit(2)

    try:
        input_file = open(input_file_name, "r")
        date_lines = input_file.read().splitlines()
        input_file.close()
    except IOError:
        print "The input file does not exist"
        sys.exit(2)

    batlog2csv = Batlog2Csv(date_lines)

    print batlog2csv.convert()


if __name__ == "__main__": main()
