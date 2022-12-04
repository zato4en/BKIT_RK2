

from operator import itemgetter
class Director:
    """Дирижер"""
    def __init__(self, id, name, salary, orch_id):
        self.id = id
        self.name = name
        self.salary = salary
        self.orch_id = orch_id
class Orchestra:
    """Оркестр"""
    def __init__(self, id, title):
        self.id = id
        self.title = title
class DirectorOrchestra:
    """
     'Дирижеры оркестров' для реализации
     связи многие-ко-многим
     """

    def __init__(self, dir_id, orch_id):
        self.dir_id = dir_id
        self.orch_id = orch_id


# Дирижеры
directors = [
    Director(1, 'Бан', 150000, 1),
    Director(2, 'Вагнер', 2800, 2),
    Director(3, 'Деймур', 100000, 2),
    Director(4, 'Ким Чен Ын', 86400, 3),
    Director(5, 'Поляков', 44444, 4)
]
# Оркестры
orchestras = [
    Orchestra(1, 'Банановая республика'),
    Orchestra(2, 'AGSPD'),
    Orchestra(3, 'BTS'),
    Orchestra(4, 'Дрилл Авиация')
]
directors_orchestras = [
    DirectorOrchestra(1, 1),
    DirectorOrchestra(2, 2),
    DirectorOrchestra(3, 3),
    DirectorOrchestra(4, 4),
    DirectorOrchestra(5, 1),
    DirectorOrchestra(5, 1),
    DirectorOrchestra(2, 3),
    DirectorOrchestra(3, 2),
    DirectorOrchestra(4, 1),
    DirectorOrchestra(5, 4)
]

one_to_many = [(dir.name, dir.salary, orch.title)
                   for orch in orchestras
                   for dir in directors
                   if dir.orch_id == orch.id]
# Соединение данных многие-ко-многим
many_to_many_temp = [(orch.title, dir.orch_id, dir.dir_id)
                     for orch in orchestras
                     for dir in directors_orchestras
                     if orch.id == dir.orch_id]
many_to_many = [(dir.name, dir.salary, orchestra_name)
                for orchestra_name, orch_id, dir_id in many_to_many_temp
                for dir in directors if dir.id == dir_id]

def task1(one_to_many):
    res = {}
    for orch in orchestras:
        if orch.title[0] == 'A':
            d_emps = list(filter(lambda i: i[2] == orch.title, one_to_many))
    d_emps_names = [x for x, _, _ in d_emps]
    res[orch.title] = d_emps_names
    return res

def task2(one_to_many):
    res2_unsorted = []
    for orch in orchestras:
        orch_Directors = list(filter(lambda i: i[2] == orch.title,
                                     one_to_many))
    if len(orch_Directors) > 0:
        orch_sals = [sal for _, sal, _ in orch_Directors]
    orch_sals_sum = max(orch_sals)
    res2_unsorted.append((orch.title, orch_sals_sum))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    return res2

def task3(many_to_many):
    res3 = sorted(many_to_many, key=itemgetter(2))
    return res3





# print('\nЗадание Г1')
# print(task1(one_to_many))
# print('\nЗадание Г2')
# print(task2(one_to_many))
# print('\nЗадание Г3')
# for i in task3(many_to_many):
#     print(i)



