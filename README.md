# Калькулятор калорий и денег

**python,  ООП**

## Описание проекта
### Калькулятор денег (класс CashCalculator):    
1. Определяет, сколько ещё денег можно потратить сегодня в рублях,  
долларах или евро — метод `get_today_cash_remained(currency)`  
2. Считает, сколько денег потрачено за последние 7 дней — метод `get_week_stats()`

  
### Калькулятор калорий (класс CaloriesCalculator):    
1. Определяет, сколько ещё калорий можно/нужно получить сегодня — метод `get_calories_remained()`
2. Считает, сколько калорий получено за последние 7 дней — метод `get_week_stats()`

Классы **CashCalculator** и **CaloriesCalculator** наследуются от класса **Calculator**. В классе **Calculator** реализован общий для двух калькуляторов функционал:

 1. Хранение записей.
 2. Дневной лимит.
 3. Суммирование записей за конкретные даты.

Конструктор класса **Calculator** принимает один аргумент — дневной лимит трат/калорий.


### Формат вывода  
 -  Метод `get_calories_remained()`  калькулятора калорий возвращает один из ответов:  
    - *Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не  
   более N кКал* (если лимит не достигнут)   
    - *Хватит есть!* (если лимит достигнут или превышен)
 
 - Метод `get_today_cash_remained(currency)`  денежного калькулятора принимает на вход код валюты (одну из строк "rub"  , "usd"  или "eur") и возвращает сообщение о состоянии дневного баланса в этой валюте,  
округляя сумму до двух знаков после запятой (до сотых):
   - *На сегодня осталось N руб/USD/Euro*  (если лимит не достигнут)  
   - *Денег нет, держись* (если лимит достигнут)
   - *Денег нет, держись: твой долг — N руб/USD/Euro* (если лимит  
   превышен)
   
### Автор
Evgenia Drobova
