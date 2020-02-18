from itertools import combinations

from classes.ExcelModule import ExcelModule
from classes.TestCaseMedicalHistoryFilter import TestCaseMedicalHistory
from classes.TestCaseJournalFilter import TestCaseJournalFilter


def make_case_journal(fields, file_name, number):
    i = 1
    case_list = []
    print(str(number) + ") Заголовок")
    print()
    print()
    while i <= 1:
        result = list(combinations(fields, i))
        index = 1
        for r in result:
            case = TestCaseJournalFilter(r)
            case.make_case()
            case_number = str(number) + '.' + str(index)
            case.show(case_number)
            case_list.append(case)
            index += 1
        i += 1
        print()
        print()
    path = 'C:\\Users\\Phantom\\Desktop\\' + file_name + '.xls'
    excel = ExcelModule(path)
    excel.make_file(case_list, number)
    excel.save_file()


def make_case_medical_history(mode, fields, file_name, number):
    i = 1
    case_list = []
    print(str(number) + ") Заголовок")
    print()
    print()
    while i <= 6:
        result = list(combinations(fields, i))
        index = 1
        for r in result:
            case = TestCaseMedicalHistory(mode, r)
            case.make_case()
            case_number = str(number) + '.' + str(index)
            case.show(case_number)
            case_list.append(case)
            index += 1
        i += 1
        print()
        print()
    path = 'C:\\Users\\Phantom\\Desktop\\' + file_name + '.xls'
    excel = ExcelModule(path)
    excel.make_file(case_list, number)
    excel.save_file()




