games = int(input("Сколько записей вносится в протокол: "))
games_result_dict = dict()

print("Записи (результат и имя")
for i_game in range(1, games +1):
    print("{} запись:".format(i_game), end=" ")
    points, player = input().split()
    if player in games_result_dict:
        if games_result_dict[player][0] < points:
            games_result_dict[player] = points, i_game
    else:
        games_result_dict[player] = points, i_game

print("Итоги соревнования: ")
games_result_list_key = []
games_result_list_value = []
for i_key, i_value in games_result_dict.items():
    games_result_list_key.append(i_key)
    games_result_list_value.append(i_value)
print(games_result_list_key, games_result_list_value)

print(games_result_dict)

# TODO, далее, необходимо создать список списков из ключей и значений словаря games_result_dict.
#  Поможет функция list и метод словарей items.
#  После этого, сможем просто пройти по списку в цикле =)