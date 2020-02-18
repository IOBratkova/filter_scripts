from classes.TestCase import TestCase, Step


class TestCaseJournalFilter(TestCase):
    def __init__(self, fields):
        super().__init__()
        self.fields = fields

    """
    Создание всего кейса
    """
    def make_case(self):
        self.make_title()
        self.make_all_steps()

    """
    Создание всех шагов
    """
    def make_all_steps(self):
        res = [self.make_first_step()]
        middle = self.make_middle_steps()
        for step in middle:
            res.append(step)
        res.append(self.make_last_step())
        self.steps = res
        return res

    """
    Заголовок
    """
    def make_title(self):
        res = 'Проверка фильтрации по '
        tmp = ''
        for f in self.fields:
            if f == '\"Прикрепление\"':
                tmp += 'блоку полей ' + f + ', '
            elif f == '\"ДН\"':
                tmp += 'чек-боксу ' + f + ', '
            else:
                tmp += 'полю ' + f + ', '
        tmp = tmp[0:-2]
        self.title = res + tmp

    """
    Первый шаг
    """
    def make_first_step(self):
        act = 'В журнале ИЭМК нажать на кнопку \"Развернуть\".'
        res = 'Убедиться, что произошло отображение панели фильтрации.\n' \
              'Убедитсья, что активны следующие поля фильтра: '
        tmp = ''
        for f in self.fields:
            if f == '\"Прикрепление\"':
                tmp += 'блок полей ' + f + ', '
            elif f == '\"ДН\"':
                tmp += 'чек-бокс ' + f + ', '
            else:
                tmp += 'поле ' + f + ', '
        tmp = tmp[0:-2]
        res += tmp
        return Step(act, res)

    """
    Последний шаг
    """
    def make_last_step(self):
        action = 'Нажать на кнопку \"Найти\".'
        result = 'Убедиться, данные в списке записей журнала ИЭМК отобразились соответствующим образом.'
        return Step(action, result)

    """
    Промежуточные шаги
    """
    def make_middle_steps(self):
        middle_steps = []
        for f in self.fields:
            if f == '\"Прикрепление\"':
                act = 'Заполнить блок полей ' + f + ' произвольным образом.'
                res = 'Убедиться, что в блоке полей ' + f + ' отображаются произвольные записи.'
            elif f == '\"ДН\"':
                act = 'Установить чек-бокс ' + f + '.'
                res = 'Убедиться, что в чек-боксе ' + f + ' отображается символ галочки.'
            else:
                act = 'Выбрать в поле ' + f + ' произвольную запись.'
                res = 'Убедиться, что в поле ' + f + ' отображается произвольная запись.'
            middle_steps.append(Step(act, res))
        return middle_steps
