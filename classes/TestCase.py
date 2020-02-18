# Класс шаг Тест-кейса
class Step:
    def __init__(self, act, res):
        self.action = act
        self.result = res

    def toString(self):
        return 'Действие: ' + self.action + '\n' + \
               'Результат: ' + self.result + '\n'


# Класс Тест-кейс
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