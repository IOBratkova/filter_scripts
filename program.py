from functions import make_case_medical_history
from data import fields_section, fields_chronology

# Создание тест-кейсов для режима "Просмотр по разделам"
make_case_medical_history('Просмотр по разделам', fields_section, 'sections', 25)

# Создание тест-кейсов для режима "Хронология"
make_case_medical_history('Хронология', fields_chronology, 'chronology', 26)
