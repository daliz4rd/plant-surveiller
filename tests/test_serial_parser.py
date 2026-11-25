from serial_parser import parse_reading


# Clean lines, as Serial.println() sends them (number + carriage return + newline)

def test_clean_line():
    assert parse_reading("512\r\n") == 512


def test_lowest_reading():
    assert parse_reading("0\r\n") == 0


def test_highest_reading():
    assert parse_reading("1023\r\n") == 1023


def test_line_without_line_ending():
    assert parse_reading("512") == 512


# Numbers the analog input can never produce

def test_above_range():
    assert parse_reading("1024\r\n") is None


def test_negative():
    assert parse_reading("-3\r\n") is None


def test_decimal():
    assert parse_reading("512.5\r\n") is None


# Lines that aren't numbers at all

def test_empty_line():
    assert parse_reading("\r\n") is None


def test_empty_string():
    assert parse_reading("") is None


def test_garbage_characters():
    assert parse_reading("Ã¿?\r\n") is None


def test_label_and_number():
    assert parse_reading("moisture: 512\r\n") is None
