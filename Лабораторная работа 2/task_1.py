money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = salary + money_capital #начальный бюджет
month = 0
while spend <= budget:
    month += 1
    budget -= spend
    budget += salary
    spend += spend * increase #траты на следующий месяц с учетом роста цен
print("Количество месяцев, которое можно протянуть без долгов:", month)
