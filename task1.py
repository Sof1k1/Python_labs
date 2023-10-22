money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    spend = (spend * increase) + spend
    take_from_capital = spend - salary
    money_capital -= take_from_capital
    month += 1
    if money_capital <= 0:
        break
print("Количество месяцев, которое можно протянуть без долгов:", month)