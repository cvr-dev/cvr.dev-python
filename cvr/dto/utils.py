from dateutil.parser import parse


def parse_date_time(v):
    if v is None:
        return None

    try:
        return parse(v)
    except ValueError:
        return None
