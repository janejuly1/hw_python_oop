import datetime as dt


class Record:
    def __init__(self,
                 amount: float,
                 comment: str,
                 date=None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
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
        today_sum = 0
        for r in self.records:
            if r.date == dt.datetime.now().date():
                today_sum += r.amount

        return today_sum

    def get_week_stats(self):
        week_ago = (dt.datetime.now() - dt.timedelta(days=7)).date()
        week_sum = 0
        for r in self.records:
            if week_ago <= r.date <= dt.datetime.now().date():
                week_sum += r.amount

        return week_sum


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def get_today_cash_remained(self, currency):
        coeff = 1
        cur_name = "руб"
        if currency == "usd":
            coeff = 1 / self.USD_RATE
            cur_name = "USD"
        elif currency == "eur":
            coeff = 1 / self.EURO_RATE
            cur_name = "Euro"

        balance = round(abs(self.limit - self.get_today_stats()) * coeff, 2)

        if self.get_today_stats() < self.limit:

            return f'На сегодня осталось {balance} {cur_name}'

        elif self.get_today_stats() == self.limit:

            return 'Денег нет, держись'

        elif self.get_today_stats() > self.limit:

            return f'Денег нет, держись: твой долг - {balance} {cur_name}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.limit - self.get_today_stats()
        if self.get_today_stats() < self.limit:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    + f'но с общей калорийностью не более {calories} кКал')

        else:
            return 'Хватит есть!'
