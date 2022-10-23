money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
def life(money_capital, salary, spend, increase):
    month = 0  # количество месяцев, которое можно прожить
    money_capital -= spend
    while money_capital > 0:
        money_capital += salary - spend
        spend *= 1 + increase
        if money_capital > 0:
            month += 1

    return month
month = life(money_capital, salary, spend, increase)

print(month)
