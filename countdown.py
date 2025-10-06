try:
    num = int(input("Введите число:\n"))

    while num >= 0:
        print(num)
        num -= 1

except ValueError:
    print("Усп, вы ввели не число! Попробуйте заново.")
