import datetime

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def format_currency(amount):
    return f"${amount:,.2f}"