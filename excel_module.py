import xlwt


class ExcelModule:
    def __init__(self, path):
        self.wb = xlwt.Workbook()  # создаем книгу
        self.ws = self.wb.add_sheet('Test')  # создаем лист
        self.path = path

    def make_file(self, test_cases, number):
        str_number = str(number)                                    # номер раздела, фиксированный
        self.ws.write(0, 0, str_number)                             # номер раздела
        row_sub_section_title = 1                                   # строка подраздела
        case_number = 1
        step_number = 1
        for case in test_cases:                                     # цикл по всем кейсам
            self.ws.write(row_sub_section_title, 0, case_number)     # пишем номер кейса
            self.ws.write(row_sub_section_title, 1, case.title)     # пишем заголовок кейса
            row_step = row_sub_section_title + 1                    # строка с шагом - следующая за заголовком
            for step in case.steps:
                self.ws.write(row_step, 0, step_number)
                self.ws.write(row_step, 2, step.action)
                self.ws.write(row_step, 3, step.result)
                step_number += 1
                row_step += 1
            case_number += 1
            row_sub_section_title += len(case.steps) + 1

    def save_file(self):
        self.wb.save(self.path)

