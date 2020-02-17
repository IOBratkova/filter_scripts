import xlwt


class ExcelModule:
    def __init__(self, path):
        self.wb = xlwt.Workbook()  # создаем книгу
        self.ws = self.wb.add_sheet('Test')  # создаем лист
        self.path = path

    def make_file(self, test_cases, number):
        self.ws.write(0, 0, number)                                 # номер раздела 5
        row_sub_section_title = 1                                   # строка подраздела
        case_number = 1                                             # номер кейса
        for case in test_cases:                                     # цикл по всем кейсам
            new_case_num = str(number) + '.' + str(case_number)     # большой номер кейса 5.1
            self.ws.write(row_sub_section_title, 0, new_case_num)   # пишем номер кейса   5.1
            self.ws.write(row_sub_section_title, 1, case.title)     # пишем заголовок кейса
            row_step = row_sub_section_title + 1                    # строка с шагом - следующая за заголовком
            step_number = 1
            for step in case.steps:
                new_step_number = new_case_num + '.' + str(step_number)
                self.ws.write(row_step, 0, new_step_number)
                self.ws.write(row_step, 2, step.action)
                self.ws.write(row_step, 3, step.result)
                step_number += 1
                row_step += 1
            case_number += 1
            row_sub_section_title += len(case.steps) + 1

    def save_file(self):
        self.wb.save(self.path)

