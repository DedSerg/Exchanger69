team1_name = "Второе дыхание"
team2_name = "La shance final"
result = 'ничья'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
# challenge_result = 'Победа команды "La shance final"!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'победа команды "{team1_name}"!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'победа команды "{team2_name}"!'
else:
    result = 'Ничья!'
print('В команде "%s" - %s участников!' % (team1_name, team1_num))
print('В команде "%s" - %s участников!' % (team2_name, team2_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

print('Команда "{}" решила задач: {}' . format(team1_name, score_1))
print('Команда "{}" решила задач: {}' . format(team2_name, score_2))
print('"{}" решили задачи за {} с !' . format (team1_name, team1_time))
print('"{}" решили задачи за {} с !' . format (team2_name, team2_time))

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {result} ')
print(f'Сегодня было решено {(score_1 + score_2)}, в среднем по {round((team1_time + team2_time) / (score_1 + score_2), 2)} секунды на задачу.')
