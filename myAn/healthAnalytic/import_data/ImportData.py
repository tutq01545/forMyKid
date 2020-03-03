from healthAnalytic import init_import
from healthAnalytic.models import Kid, Country, Activity, InformationPerPeriod
from datetime import datetime


class Importer:

    @staticmethod
    def import_kid_data(first_name: str, last_name: str, birth_date: str, birth_place: str):
        try:
            Kid.objects.update_or_create(
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                birth_place=birth_place
            )
        except Exception as e:
            print(e)

    @staticmethod
    def import_country_data(country_name: str, country_code: str):
        try:
            Country.objects.update_or_create(
                country_name=country_name,
                country_code=country_code
            )
        except Exception as e:
            print(e)

    @staticmethod
    def import_activity_data(activity_name: str, calculation_mass: str):
        try:
            Activity.objects.update_or_create(
                activity_name=activity_name,
                calculation_mass=calculation_mass
            )
        except Exception as e:
            print(e)

    @staticmethod
    def import_information_per_period_data(kid: Kid, date: datetime, from_to: str,
                                           activity: Activity, quantity: int, comment: str):
        try:
            InformationPerPeriod.objects.update_or_create(
                kid=kid,
                date=date,
                from_to=from_to,
                activity=activity,
                quantity=quantity,
                comment=comment
            )
        except Exception as e:
            print(e)
