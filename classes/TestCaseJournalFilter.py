from classes.TestCase import TestCase, Step


class TestCaseJournalFilter(TestCase):
    def __init__(self, fields):
        super().__init__()
        self.fields = fields

    """
    Создает полный кейс.
    """
    def make_case(self):
        self.make_title()
        self.make_all_steps()

    """
    Создает заголовок кейса.
    """
    def make_title(self):
        s = self.fieldsToString()
        self.title = 'Проверка фильтрации по '
        if len(self.fields) == 1:
            self.title += 'полю ' + s
        else:
            self.title += 'полям ' + s
        self.title += ' в журнале ИЭМК'

    """
    Создает все шаги кейса.
    """
    def make_all_steps(self):
        first = self.make_first_step()
        second = self.make_middle_step()
        last = self.make_last_step()
        res = [first]
        for s in second:
            res.append(s)
        res.append(last)
        self.steps = res
        return res

    """
    Превращает список полей в строку
    """
    def fieldsToString(self):
        result = ''
        for f in self.fields:
            result += f
        result = result[0:-2]
        return result

    """
    Первый шаг: 
    В журнале ИЭМК нажать на кнопку "Развернуть".
    Убедиться, что поля фильтра активны.
    """
    def make_first_step(self):
        action = 'В журнале ИЭМК нажать на кнопку \"Развернуть\"'
        result = 'Убедиться, что произошло отображение панели фильтрации.'
        string_fields = self.fieldsToString()
        if len(self.fields) == 1:
            result += '\nУбедиться, что поле фильтра ' + string_fields + ' активно.'
        else:
            result += '\nУбедиться, что поля фильтра ' + string_fields + 'активны.'
        return Step(action, result)

    """
    Последний шаг:
    Нажать на кнопку "Найти"
    Убедиться, что фильтрация произошла согласно поля/полей таких-то
    """
    def make_last_step(self):
        action = 'Нажать на кнопку \"Найти\"'
        result = 'Убедиться, что фильтрация списка записей произошла согласно '
        string_fields = self.fieldsToString()
        if len(self.fields) == 1:
            result += 'поля ' + string_fields + '.'
        else:
            result += 'полей ' + string_fields + '.'
        return Step(action, result)

    """
    Промежуточные шаги:
    Выбрать в поле такое-то произвольную запись.
    Убедитсья, что в поле таком-то отображается произвольная запись.
    """
    def make_middle_step(self):
        steps = []
        for f in self.fields:
            action = 'Выбрать в поле ' + f + ' произвольную запись.'
            result = 'Убедиться, что в поле ' + f + ' отображается произвольная запись.'
            steps.append(Step(action, result))
        return steps
