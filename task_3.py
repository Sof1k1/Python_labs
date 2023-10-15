list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_of_players = len(list_players)
team1 = list_players[:int(count_of_players / 2):]
team2 = list_players[int(count_of_players / 2)::]
print(team1)
print(team2)