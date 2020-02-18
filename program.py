from functions import make_case_medical_history, make_case_journal
from data import fields_section, fields_chronology, fields_journal

# Создание тест-кейсов для режима "Просмотр по разделам"
make_case_medical_history('Просмотр по разделам', fields_section, 'sections', 25)

# Создание тест-кейсов для режима "Хронология"
make_case_medical_history('Хронология', fields_chronology, 'chronology', 26)

# Создание тестов для журнала
make_case_journal(fields_journal, 'journal', 27)

