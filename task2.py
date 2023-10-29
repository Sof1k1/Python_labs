def find_common_participants(first_group, second_group, separator=','):
    participants1 = first_group.split(separator)
    participants2 = second_group.split(separator)
    set1 = set(participants1)
    set2 = set(participants2)
    common_participants = set1.intersection(set2)
    result = sorted(list(common_participants))
    return result


participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator=',')
print(common_participants)