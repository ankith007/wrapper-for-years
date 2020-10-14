import datetime


def generate_dates(a_start_date, a_end_date):
    start_date = datetime.datetime.strptime(a_start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(a_end_date, "%Y-%m-%d")
    dates_generated = [start_date + datetime.timedelta(days=x) for x in range(0, (end_date - start_date).days + 1)]
    return dates_generated
