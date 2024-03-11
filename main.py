def programmer(n):
    if n % 100 in range(11, 20):  # для чисел від 11 до 19 закінчення "програмістів".
        return str(n) + ' програмістів'
    elif n % 10 == 1:
        return str(n) + ' програміст'
    elif n % 10 in range(2, 5):
        return str(n) + ' програміста'
    else:
        return str(n) + ' програмістів'

n = int(input("Кількість програмістів: "))

print(programmer(n))
