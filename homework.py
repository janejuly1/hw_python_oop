import datetime as dt


class Record:
    def __init__(self,
                 amount: float,
                 comment: str,
                 date=None) -> None:
        self.amount = amount
        self.comment = comment

        if date is None:
            self.date = dt.date.today()
        elif type(date) == str:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = date


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.date.today()

        return sum(record.amount for record in self.records
                   if record.date == today)

    def get_week_stats(self):
        week_ago = (dt.datetime.now() - dt.timedelta(days=7)).date()
        today = dt.date.today()

        return sum(record.amount for record in self.records
                   if week_ago <= record.date <= today)

    def today_remained(self):
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def get_today_cash_remained(self, currency):
        currency_dict = {
            "rub": {"coeff": 1.0, "name": "руб"},
            "usd": {"coeff": self.USD_RATE, "name": "USD"},
            "eur": {"coeff": self.EURO_RATE, "name": "Euro"},
        }

        if currency not in currency_dict.keys():
            return None

        today_remained = self.today_remained()

        if today_remained == 0:
            return 'Денег нет, держись'

        balance = round(abs(today_remained)
                        / currency_dict[currency]["coeff"], 2)

        if today_remained > 0:
            return (f'На сегодня осталось {balance} '
                    + f'{currency_dict[currency]["name"]}')

        else:
            return (f'Денег нет, держись: твой долг - {balance} '
                    + f'{currency_dict[currency]["name"]}')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_calories = self.today_remained()

        if today_calories > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    + 'но с общей калорийностью не более '
                    + f'{today_calories} кКал')

        else:
            return 'Хватит есть!'
