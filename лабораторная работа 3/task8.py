money_capital = 10000 # подушка безопасности в рублях
salary = 5000 # зп
spend = 6000 # расходы на проживание
increase = 0.05 # рост цен увеличивает на столько расходы

month = 0  # количество месяцев
delta = salary - spend
while money_capital >= spend:
    money_capital = money_capital + salary - spend
    spend = spend * (1+increase)**month
    month += 1

print(month)

# TODO Оформить решение


