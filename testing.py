import unittest
import sys,os

sys.path.append(os.getcwd()) #current working directory
from main import *
from main import task1, task2, task3
from main import one_to_many, many_to_many


class TestTask1(unittest.TestCase):
    def test_task_1(self):
        res = task1(one_to_many)
        expected = {'Дрилл Авиация': ['Вагнер', 'Деймур']}
        self.assertEqual(res, expected)

class TestTask2(unittest.TestCase):
    def test_task_2(self):
        res = task2(one_to_many)
        expected = [('Дрилл Авиация', 44444)]
        self.assertEqual(res, expected)


class TestTask3(unittest.TestCase):
    def test_task_3(self):
        res = task3(many_to_many)
        expected = [('Вагнер', 2800, 'AGSPD'),
                    ('Деймур', 100000, 'AGSPD'),
                    ('Деймур', 100000, 'BTS'),
                    ('Вагнер', 2800, 'BTS'),
                    ('Бан', 150000, 'Банановая республика'),
                    ('Поляков', 44444, 'Банановая республика'),
                    ('Поляков', 44444, 'Банановая республика'),
                    ('Ким Чен Ын', 86400, 'Банановая республика'),
                    ('Ким Чен Ын', 86400, 'Дрилл Авиация'),
                    ('Поляков', 44444, 'Дрилл Авиация')]
        self.assertEqual(res, expected)



if __name__=='__main__':
    unittest.main()