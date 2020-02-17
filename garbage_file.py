from itertools import combinations

titles = ['\"c\" группы полей \"Период\"', '\"по\" группы полей \"Период\"', '\"Медицинская организация\"', '\"Регистр\"',
          '\"Врач\"', '\"Диагноз\"']


# Заголовок фильтра
def make_case_title(tup):
    s = ''
    for t in tup:
        s += 'полю ' + t + ', '
    s = s[0: -2]
    return 'Проверка фильтрации по ' + s + ' в \"Фильтре медицинской истории\"'


# Первый шаг
def make_first_step():
    return ('Открыть ИЭМК произвольного пациента.', 'Убедиться, что ИЭМК произвольного пациента открывается. '
                                                    'Убедиться, что между разделами \"Персональные данные\" и '
                                                    '\"Аллергия\" '
                                                    'располагается фильтр отображения записей \"Фильтр медицинской '
                                                    'истории\".')


def make_second_step(tup):
    s1 = ''
    s2 = ''
    result = []
    for l in tup:
        s1 = 'Выбрать в поле ' + l + ' произвольную запись.'
        s2 = 'Убедиться что в поле ' + l + ' отображается произвольная запись.'
        result.append((s1, s2))
    return result


# третий шаг кейса
def make_third_step():
    return 'Нажать на кнопку \"Найти\"', 'Убедиться, что данные в разделах отобразились согласно фильтру.'


def make_all_steps(tup):
    first = make_first_step()
    second = make_second_step(tup)
    last = make_third_step()
    res = [first]
    for s in second:
        res.append(s)
    res.append(last)
    return res


def print_test_case(title, step_list):
    print(title) # печатаем заголовок
    n = len(step_list) # узнаем кол-во шагов
    i = 0
    while i < n:
        action = 'Действие: ' + steps[i][0]
        result = 'Результат: ' + steps[i][1]
        print('- ' + action)
        print(result)
        i += 1


# program
i = 1
while i <= 6:
    result = list(combinations(titles, i))  # Создаем комбинацию из 6 по i [(), (), ()]
    for r in result:
        case_title = make_case_title(r)  # Создаем заголовок кейса
        steps = make_all_steps(r)
        print_test_case(case_title, steps)
        print()
    print()
    print()

    i += 1