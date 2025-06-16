from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        delta_days = today - input_date
        return print(delta_days.days)
    except ValueError:
        raise ValueError ("Невірний формат дати. Використовуйте РРРР-ММ-ДД")
    
get_days_from_today("1981-03-15")

    