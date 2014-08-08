import csv
import unittest

from batlog2csv import Batlog2Csv


class TestConvert(unittest.TestCase):
    def test_that_standard_log_is_parsed_correctly(self):
        csv = self.get_csv("data/default.dat")

        header = csv.next()
        row = csv.next()

        self.check_header(header)
        self.assertEqual(row[0], "2012-08-14 10:41:46")
        self.assertEqual(row[1], "1")
        self.assertEqual(row[2], "6667")
        self.assertEqual(row[3], "6329")
        self.assertEqual(row[4], "6700")

    def test_that_standard_log_is_parsed_correctly(self):
        csv = self.get_csv("data/wrongorder.dat")

        header = csv.next()
        row = csv.next()

        self.check_header(header)
        self.assertEqual(row[0], "2014-08-07 00:15:00")
        self.assertEqual(row[1], "19")
        self.assertEqual(row[2], "8532")
        self.assertEqual(row[3], "8532")
        self.assertEqual(row[4], "8440")

    def check_header(self, header):
        self.assertEqual(header[0], "Date")
        self.assertEqual(header[1], "CycleCount")
        self.assertEqual(header[2], "MaxCapacity")
        self.assertEqual(header[3], "CurrentCapacity")
        self.assertEqual(header[4], "DesignCapacity")

    def get_csv(self, file_path):
        with open(file_path) as data_file:
            return csv.reader(Batlog2Csv(
                data_file.read().splitlines()).convert().strip().split("\n"))


if __name__ == '__main__':
    unittest.main()
