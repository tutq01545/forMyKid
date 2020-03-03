from dateutil import parser
from datetime import datetime
import pandas as pd


def convert_str_to_date(date: str) -> datetime:
    """Convert from string date to datetime object


    :param:
        date (str): a date of type string

    :return:
        a datetime object


    """
    return parser.parse(date)


def __correct_name_input(name: str) -> str:
    """Correct string input for name when reading Excel template


    :param
        name (str): string input for name (first name, last name)
    :return:
        a stripped string, first character in each word is capitalized


    """

    try:
        return name.strip().title()
    except AttributeError:
        print("Attribute Error, when correcting name input for {}".format(name))
        return ""


def __correct_string_input(string_input:str) -> str:
    """Correct string input when reading Excel template


    :param
        name (str): string input ('Activity', 'From to', 'Quantity')
    :return:
        a stripped string, first character in each word is capitalized


    """
    try:
        return string_input.strip()
    except AttributeError:
        print("Attribute Error, when correcting name input for {}".format(string_input))
        return ""


def read_data_from_excel_file(file: str) -> pd.DataFrame:
    """Read excel file


    :param:
        file: a string contains file name with full path


    :return:
        a DataFrame object


    """
    __columns = ["First name", "Last name", "Birth date", 'Date', "From to", "Activity", "Quantity", "Comment"]
    with open(file, "rb") as excel_file:
        data_frame = pd.read_excel(excel_file)
        __return = []

        if not data_frame.empty:

            # Convert string birth date to datetime object
            try:
                data_frame['Birth date'] = pd.to_datetime(data_frame['Birth date'], dayfirst=True)
            except pd.tslib.OutOfBoundsDatetime:
                pass
            except Exception as e:
                print(e)

            try:
                data_frame['Date'] = pd.to_datetime(data_frame['Date'], dayfirst=True)
            except pd.tslib.OutOfBoundsDatetime:
                pass
            except Exception as e:
                print(e)

            # Iterate over row
            for index, row in data_frame.iterrows():
                first_name = __correct_name_input(row['First name'])
                last_name = __correct_name_input(row['Last name'])
                birth_date = row['Birth date']
                date = row['Date']
                from_to = __correct_string_input(row['From to'])
                activity = __correct_string_input(row['Activity'])

                str_quantity = __correct_string_input(row['Quantity'])
                try:
                    quantity = int(str_quantity)
                except ValueError:
                    print("ValueError when converting quantity in data frame")
                    quantity = 0

                comment = __correct_string_input(row['Comment'])

                __return.append(
                    {
                        'first name': first_name,
                        'last name': last_name,
                        'birth date': birth_date,
                        'date': date,
                        'from to': from_to,
                        'activity': activity,
                        'quantity': quantity,
                        'comment': comment
                    }
                )

        excel_file.close()
        return __return
