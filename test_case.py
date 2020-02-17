class Step:
    def __init__(self, act, res):
        self.action = act
        self.result = res

    def toString(self):
        return 'Действие: ' \
               + self.action + '\nРезультат: ' \
               + self.result


class TestCase:
    def __init__(self):
        self.title = ''
        self.steps = []

    def setTitle(self, title):
        self.title = title

    def setSteps(self, steps):
        self.steps = steps

    def show(self, case_number):
        print(self.toString(case_number))

    def toString(self, case_number):
        s = case_number + ') ' + self.title + '\n'
        i = 1
        for step in self.steps:
            step_number = case_number + '.' + str(i)
            tmp = step.toString()
            s += step_number + ') ' + tmp + '\n'
            i += 1
        return s


class TestCaseOfMedicalHistorySection(TestCase):
    def __init__(self):
        super().__init__()

    def make_case(self, field):
        self.make_title(field)
        self.make_all_steps(field)

    def make_title(self, field):
        s = ''
        for f in field:
            s += 'полю ' + f + ', '
        s = s[0: -2]
        self.title = 'Проверка фильтрации по ' + s + \
                     ' в \"Фильтре медицинской истории\" ' \
                     'в режиме \"Просмотр по разделам\"'

    def make_loop_steps(self, field):
        result = []
        for f in field:
            act = 'Выбрать в поле ' + f + ' произвольную запись.'
            res = 'Убедиться что в поле ' + f + ' отображается произвольная запись.'
            step = Step(act, res)
            result.append(step)
        return result

    def make_last_step(self):
        act = 'Нажать на кнопку \"Найти\"'
        res = 'Убедиться, что данные в разделах отобразились согласно фильтру.'
        return Step(act, res)

    def make_first_step(self):
        act = 'Открыть ИЭМК произвольного пациента.'
        res = 'Убедиться, что ИЭМК произвольного пациента открывается. ' \
              'Убедиться, что между разделами \"Персональные данные\" и ' \
              '\"Аллергия\" располагается фильтр отображения записей ' \
              '\"Фильтр медицинской истории\".'
        return Step(act, res)

    def make_all_steps(self, field):
        first = self.make_first_step()
        second = self.make_loop_steps(field)
        last = self.make_last_step()
        res = [first]
        for s in second:
            res.append(s)
        res.append(last)
        self.steps = res
        return res
