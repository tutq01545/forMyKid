from healthAnalytic.helper.help_function import convert_str_to_date


def test_convert_str_to_date():
    input_date = "25.12.2019"
    output_date_datetime = convert_str_to_date(input_date)
    output_date_str = "{}.{}.{}".format(output_date_datetime.day, output_date_datetime.month, output_date_datetime.year)

    assert output_date_str == input_date


if __name__ == '__main__':
    test_convert_str_to_date()