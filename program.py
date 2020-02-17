from itertools import combinations

from excel_module import ExcelModule
from test_case import TestCaseOfMedicalHistorySection
import xlwt


fields = ['\"c\" группы полей \"Период\"',
          '\"по\" группы полей \"Период\"',
          '\"Медицинская организация\"',
          '\"Регистр\"',
          '\"Врач\"',
          '\"Диагноз\"']

i = 1
case_list = []
number = 5
print(str(number) + ") Заголовок")
print()
print()
while i <= 6:
    result = list(combinations(fields, i))
    index = 1
    for r in result:
        case = TestCaseOfMedicalHistorySection()
        case.make_case(r)
        case_number = str(number) + '.' + str(index)
        case.show(case_number)
        case_list.append(case)
        index += 1
    i += 1
    print()
    print()


path = 'C:\\Users\\Phantom\\Desktop\\tmp.xls'
excel = ExcelModule(path)
excel.make_file(case_list, number)
excel.save_file()