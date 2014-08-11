from batlog2csv import Batlog2Csv


def test_external_connected_value_is_converted_correctly_if_original_value_is_yes():
    key = Batlog2Csv.EXTERNAL_CONNECTED_KEY
    value = "Yes"
    converted_value = "true"

    assert Batlog2Csv.get_converted_value(key, value) == converted_value


def test_external_connected_value_is_converted_correctly_if_original_value_is_no():
    key = Batlog2Csv.EXTERNAL_CONNECTED_KEY
    value = "No"
    converted_value = "false"

    assert Batlog2Csv.get_converted_value(key, value) == converted_value


def test_value_is_untouched_if_it_should_not_be_converted():
    key = Batlog2Csv.CYCLE_COUNT_KEY
    value = "test"
    converted_value = "test"

    assert Batlog2Csv.get_converted_value(key, value) == converted_value