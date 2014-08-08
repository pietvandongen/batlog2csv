import csv
import unittest

from batlog2csv import Batlog2Csv


class TestConvert(unittest.TestCase):
    def test_that_standard_log_is_parsed_correctly(self):
        csv = self.get_csv("data/default.dat")

        header = csv.next()
        row = csv.next()

        self.assertEqual(header[0], "Date")
        self.assertEqual(header[1], "CycleCount")
        self.assertEqual(header[2], "MaxCapacity")
        self.assertEqual(header[3], "CurrentCapacity")
        self.assertEqual(header[4], "DesignCapacity")

        self.assertEqual(row[0], "2012-08-14 10:41:46")
        self.assertEqual(row[1], "1")
        self.assertEqual(row[2], "6667")
        self.assertEqual(row[3], "6329")
        self.assertEqual(row[4], "6700")

    def get_csv(self, file_path):
        with open(file_path) as data_file:
            return csv.reader(Batlog2Csv(data_file.read().splitlines()).convert().strip().split("\n"))


if __name__ == '__main__':
    unittest.main()
