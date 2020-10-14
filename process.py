
def generate_date_attributes(date):
    date_with_attributes = (date.strftime("%Y-%m-%d"),)
    return date_with_attributes


def generate_dates_with_attributes(dates):
    dates_with_attributes = map(
        lambda date: generate_date_attributes(date),
        dates
    )
    return list(dates_with_attributes)
