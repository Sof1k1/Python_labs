list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_of_players = len(list_players)
center_of_list = int(count_of_players // 2)
team1 = list_players[:center_of_list]
team2 = list_players[center_of_list:]
print(team1)
print(team2)
