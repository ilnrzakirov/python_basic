
summ = 0
count = 0

try:
    while summ < 777:
        number = int(input("Введите число: "))
        count += 1
        if count == 13:
            raise ("Случайная ошибка")
        res_file = open("res.txt", "a")
        res_file.write("{} \n".format(str(number)))
        summ += number
finally:
    res_file.close()
