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
        row = {}
        number_of_columns = 0

        for lineNumber, line in enumerate(self.dataLines):
            key, value, is_date = self.get_key_value_and_date(line)

            # Add value to row
            if value:
                is_new_row = is_date and row

                if is_new_row:
                    # Print header
                    if rowcount == 0:
                        number_of_columns = len(header)
                        csv += self.OUTPUT_VALUE_DELIMITER.join(header) + "\n"

                    # Append row if it has correct number of columns
                    if len(row) == number_of_columns:
                        csv += self.OUTPUT_VALUE_DELIMITER.join((row[key] for key in header if key in row)) + "\n"

                    # Start a new row
                    row = {}
                    rowcount += 1
                    column_count = 0

                do_append_key = rowcount == 0
                if do_append_key:
                    header.append(key)

                # Append value to row
                if column_count < len(header) and key in header:
                    row[key] = str(self.get_converted_value(key, value))

                column_count += 1

        # Return CSV, including the last row
        return csv + self.OUTPUT_VALUE_DELIMITER.join((row[key] for key in header if key in row)) + "\n"

    @staticmethod
    def get_key_value_and_date(line):
        is_date = False
        key = Batlog2Csv.get_key(line)

        if key in Batlog2Csv.DESIRED_COLUMNS:
            value = line[line.find(Batlog2Csv.INPUT_VALUE_DELIMITER) + len(Batlog2Csv.INPUT_VALUE_DELIMITER):]
        else:
            key, value, is_date = Batlog2Csv.parse_date(line)

        return key, value, is_date

    @staticmethod
    def get_key(line):
        return line[
            line.find(Batlog2Csv.INPUT_KEY_DELIMITER) + len(Batlog2Csv.INPUT_KEY_DELIMITER):
            line.find(Batlog2Csv.INPUT_VALUE_DELIMITER)
        ]

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

        # For dates like "Sun Mar 29 10:28:00 EEST 2015"
        try:
            value = datetime.datetime.strptime(
                string[:20] + string[24:],
                "%a %b %d %H:%M:%S %Y"
            )
        except:
            pass

        if value:
            key = Batlog2Csv.DATE_KEY
            is_date = True

        return key, value, is_date

    @staticmethod
    def get_converted_value(key, value):
        if key == Batlog2Csv.EXTERNAL_CONNECTED_KEY:
            if value == "Yes":
                return "true"
            else:
                return "false"

        return value


def main():
    try:
        input_file_name = str(sys.argv[1])
    except IndexError:
        print("Error: please provide an input file name")
        sys.exit(2)

    try:
        input_file = open(input_file_name, "r")
        date_lines = input_file.read().splitlines()
        input_file.close()
    except IOError:
        print("The input file does not exist")
        sys.exit(2)

    batlog2csv = Batlog2Csv(date_lines)

    print(batlog2csv.convert())


if __name__ == "__main__":
    main()
