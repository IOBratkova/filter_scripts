from classes.TestCase import TestCase, Step


class TestCaseMedicalHistory(TestCase):
    def __init__(self, mode, fields):
        super().__init__()
        self.mode = mode
        self.fields = fields

    def make_case(self):
        self.make_title()
        self.make_all_steps()

    def make_last_step(self):
        act = 'Нажать на кнопку \"Найти\"'
        res = 'Убедиться, что данные в разделах отобразились согласно фильтру.'
        return Step(act, res)

    def make_title(self):
        s = ''
        for f in self.fields:
            s += 'полю ' + f + ', '
        s = s[0: -2]
        self.title = 'Проверка фильтрации по ' + s + \
                     ' в \"Фильтре медицинской истории\" ' \
                     'в режиме \"' + self.mode + '\"'

    def make_loop_steps(self):
        result = []
        for f in self.fields:
            act = 'Выбрать в поле ' + f + ' произвольную запись.'
            res = 'Убедиться что в поле ' + f + ' отображается произвольная запись.'
            step = Step(act, res)
            result.append(step)
        return result

    def make_first_step(self):
        act = 'Открыть ИЭМК произвольного пациента.'
        res = 'Убедиться, что ИЭМК произвольного пациента открывается. ' \
              'Убедиться, что между разделами \"Персональные данные\" и ' \
              '\"Аллергия\" располагается фильтр отображения записей ' \
              '\"Фильтр медицинской истории\".'
        return Step(act, res)

    def make_all_steps(self):
        first = self.make_first_step()
        second = self.make_loop_steps()
        last = self.make_last_step()
        res = [first]
        for s in second:
            res.append(s)
        res.append(last)
        self.steps = res
        return res
