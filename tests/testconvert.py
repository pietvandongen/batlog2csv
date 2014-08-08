import csv
import os
from os.path import dirname, abspath

from batlog2csv import Batlog2Csv

baseDir = dirname(abspath(__file__)) + os.path.sep


def test_that_standard_log_is_parsed_correctly():
    table = get_csv(baseDir + "/data/default.dat")

    header = table.next()
    row = table.next()

    check_header(header)
    assert row[0] == "2012-08-14 10:41:46"
    assert row[1] == "1"
    assert row[2] == "6667"
    assert row[3] == "6329"
    assert row[4] == "6700"


def test_that_wrongly_ordered_log_is_parsed_correctly():
    table = get_csv(baseDir + "/data/wrongorder.dat")

    header = table.next()
    row = table.next()

    check_header(header)
    assert row[0] == "2014-08-07 00:15:00"
    assert row[1] == "19"
    assert row[2] == "8532"
    assert row[3] == "8532"
    assert row[4] == "8440"


def check_header(header):
    assert header[0] == "Date"
    assert header[1] == "CycleCount"
    assert header[2] == "MaxCapacity"
    assert header[3] == "CurrentCapacity"
    assert header[4] == "DesignCapacity"


def get_csv(file_path):
    with open(file_path) as data_file:
        return csv.reader(Batlog2Csv(
            data_file.read().splitlines()).convert().strip().split("\n"))
