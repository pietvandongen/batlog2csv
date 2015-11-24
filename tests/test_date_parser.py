from batlog2csv import Batlog2Csv


def test_that_standard_date_is_parsed_correctly():
    date_string = "Mon Sep 12 13:29:00 CDT 2013"
    year = 2013
    month = 9
    day = 12
    hour = 13
    minute = 29
    second = 0

    key, parsed_date, is_date = Batlog2Csv.parse_date(date_string)

    assert is_date
    assert parsed_date.year == year
    assert parsed_date.month == month
    assert parsed_date.day == day
    assert parsed_date.hour == hour
    assert parsed_date.minute == minute
    assert parsed_date.second == second


def test_that_date_with_timezone_as_last_part_is_parsed_correctly():
    date_string = "Fri 16 Aug 2013 21:47:02 BST"
    year = 2013
    month = 8
    day = 16
    hour = 21
    minute = 47
    second = 2

    key, parsed_date, is_date = Batlog2Csv.parse_date(date_string)

    assert is_date
    assert parsed_date.year == year
    assert parsed_date.month == month
    assert parsed_date.day == day
    assert parsed_date.hour == hour
    assert parsed_date.minute == minute
    assert parsed_date.second == second


def test_that_date_with_eet_timezone_is_parsed_correctly():
    date_string = "Sat Mar 28 12:58:00 EET 2015"
    year = 2015
    month = 3
    day = 28
    hour = 12
    minute = 58
    second = 0

    key, parsed_date, is_date = Batlog2Csv.parse_date(date_string)

    assert is_date
    assert parsed_date.year == year
    assert parsed_date.month == month
    assert parsed_date.day == day
    assert parsed_date.hour == hour
    assert parsed_date.minute == minute
    assert parsed_date.second == second


def test_that_date_with_eest_timezone_is_parsed_correctly():
    date_string = "Sun Mar 29 10:28:00 EEST 2015"
    year = 2015
    month = 3
    day = 29
    hour = 10
    minute = 28
    second = 0

    key, parsed_date, is_date = Batlog2Csv.parse_date(date_string)

    assert is_date
    assert parsed_date.year == year
    assert parsed_date.month == month
    assert parsed_date.day == day
    assert parsed_date.hour == hour
    assert parsed_date.minute == minute
    assert parsed_date.second == second


def test_that_standard_datetime_string_is_parsed_correctly():
    date_string = "2013-11-05 18:11:00"
    year = 2013
    month = 11
    day = 5
    hour = 18
    minute = 11
    second = 0

    key, parsed_date, is_date = Batlog2Csv.parse_date(date_string)

    assert is_date
    assert parsed_date.year == year
    assert parsed_date.month == month
    assert parsed_date.day == day
    assert parsed_date.hour == hour
    assert parsed_date.minute == minute
    assert parsed_date.second == second


def test_that_non_date_string_is_not_converted_to_date():
    date_string = "123"
    key, parsed_date, is_date = Batlog2Csv.parse_date(date_string)

    assert not parsed_date
    assert not is_date


def test_that_none_value_is_not_converted_to_date():
    date_string = None
    key, parsed_date, is_date = Batlog2Csv.parse_date(date_string)

    assert not parsed_date
    assert not is_date
