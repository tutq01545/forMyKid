from healthAnalytic import init_import
from myAn.settings import MEDIA_ROOT
import os
from healthAnalytic.import_data.ImportData import Importer
from healthAnalytic.helper.help_function import convert_str_to_date, read_data_from_excel_file
from healthAnalytic.models import Kid, Activity
__importer = Importer()


def one_time_import_country():
    import pycountry
    all_countries = pycountry.countries
    for country in all_countries:
        country_name = country.name
        country_code = country.alpha_2
        __importer.import_country_data(country_name=country_name, country_code=country_code)


def import_kid():
    birth_date = convert_str_to_date("25.12.2019")
    __importer.import_kid_data(first_name="An My", last_name="Tran",
                               birth_date=birth_date, birth_place="Frankfurt am Main")


def import_activity():
    __importer.import_activity_data(activity_name="sleep", calculation_mass="hour")
    __importer.import_activity_data(activity_name="eat", calculation_mass="ml")
    __importer.import_activity_data(activity_name="play", calculation_mass="hour")


def import_information_per_period_from_excel():
    __FILE_NAME = "test.xlsx"
    file_path = os.path.join(MEDIA_ROOT, __FILE_NAME)
    data = read_data_from_excel_file(file_path)
    for data_obj in data:
        try:
            relevant_kid = Kid.objects.get(first_name=data_obj['first name'], last_name=data_obj['last name'])
        except Kid.MultipleObjectsReturned:
            print("MultipleObjectsReturned for kid {} {}".format(data_obj['first name'], data_obj['last name']))
            relevant_kid = None
        except Kid.DoesNotExist:
            print("DoesNotExist for kid {} {}".format(data_obj['first name'], data_obj['last name']))
            relevant_kid = None

        try:
            relevant_activity = Activity.objects.get(activity_name=data_obj['activity'])
        except Activity.DoesNotExist:
            print("DoesNotExist for activity {}".format(data_obj['activity']))
            relevant_activity = None

        if relevant_kid is not None and relevant_activity is not None:
            __importer.import_information_per_period_data(kid=relevant_kid,
                                                          date=data_obj['date'],
                                                          from_to=data_obj['from to'],
                                                          activity=relevant_activity,
                                                          quantity=data_obj['quantity'],
                                                          comment=data_obj['comment'])
