import datetime as dt
from datetime import timedelta
from read import generate_dates
from process import generate_dates_with_attributes
from connect_ion import connect


def execute(table_name, start_date, end_date):
    print("starts")
    dates_generated = generate_dates(a_start_date=start_date, a_end_date=end_date)
    dates_with_attributes = generate_dates_with_attributes(dates_generated)
    connect(table_name, dates_with_attributes)
    print("loaded")


def start_dates(year):
    return dt.datetime.strptime(str(year), "%Y").strftime("%Y-%m-%d")


def end_dates(start_date):
    start_s_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
    t = (start_s_date + timedelta(days=364)).strftime("%Y-%m-%d")
    return t


def date_format(table_name, year=None, years=None, start_year=None, end_year=None):
    """" this is a wrapper to get single year or list of years or start year and end year """
    if year:

        start_date = start_dates(year)
        end_date = end_dates(start_date)
        execute(table_name, start_date, end_date)



    if years:
        for i in years:
            start_date = start_dates(i)
            end_date = end_dates(start_date)
            execute(table_name, start_date, end_date)

    if start_year and end_year:
        start_date = start_dates(start_year)
        end_date = start_dates(end_year)
        execute(table_name, start_date, end_date)


date_format(table_name='year_dates', years=['2005','2004'])
