from itertools import combinations
from test_case import TestCaseOfMedicalHistory
import xlwt


fields = ['\"c\" группы полей \"Период\"',
          '\"по\" группы полей \"Период\"',
          '\"Медицинская организация\"',
          '\"Регистр\"',
          '\"Врач\"',
          '\"Диагноз\"']
path = 'C:\\Users\\Phantom\\Desktop\\tmp.xls'

wb = xlwt.Workbook()        # создаем книгу
ws = wb.add_sheet('Test')   # создаем лист
ws.col(1).width = 10477
ws.col(2).width = 9314
ws.col(3).width = 9314
i = 1
row_title = 3
column_title = 1
while i <= 6:
    result = list(combinations(fields, i))
    for r in result:
        print(str(i) + ': ')
        case = TestCaseOfMedicalHistory()
        case.make_case(r)                   # забахали тест кейс
        case.show()                         # показали
        ws.write(row_title, column_title, case.title)
        row_step = row_title + 1            # строка с шагом - следующая за заголовком
        count_steps = len(case.steps)
        j = 0
        while j < count_steps:
            ws.write(row_step, 2, case.steps[j].action)
            ws.write(row_step, 3, case.steps[j].result)
            j += 1
            row_step += 1
        row_title += count_steps + 1
    i += 1
wb.save(path)
