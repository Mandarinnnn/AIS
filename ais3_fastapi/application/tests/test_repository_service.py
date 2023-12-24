import unittest
import random
from application.config import SessionLocal
from application.services.repository_service import *

"""
   Данный модуль реализует "тестовые случаи/ситуации" для модуля repository_service.
   Для создания "тестового случая" необходимо создать отдельный класс, который наследует 
   базовый класс TestCase. Класс TestCase предоставляется встроенным 
   в Python модулем для тестирования - unittest.

   Более детально см.: https://pythonworld.ru/moduli/modul-unittest.html
"""


class TestRobotRepositoryService(unittest.TestCase):
    """ Все тестовые методы в классе TestCase (по соглашению)
        должны начинаться с префикса test_* """

    def setUp(self):
        """ Наследуемый метод setUp определяет инструкции,
            которые должны быть выполнены ПЕРЕД тестированием """
        self.session = SessionLocal()  # создаем сессию подключения к БД
        try:
            pass
        except:
            print('Test data already created')

    def test_create_loading_point(self):
        """ Тест функции создания пункта загрузки"""
        result = create_loading_point(self.session,
                                      position_x=random.randint(1, 50),
                                      position_y=random.randint(1, 50),
                                      status=1
                                      )
        self.assertTrue(result)  # валидируем результат (result == True)

    def test_create_unloading_point(self):
        """Тест функции создания пункта разгрузки"""
        result = create_unloading_point(self.session,
                                        position_x=random.randint(1, 50),
                                        position_y=random.randint(1, 50),
                                        status=2
                                        )
        self.assertTrue(result)  # валидируем результат (result == True)

    def test_create_robot(self):
        """ Тест функции создания записи Robot """
        result = create_robot(self.session,
                              charge=100,
                              position_x=random.randint(1, 50),
                              position_y=random.randint(1, 50),
                              r_state=1,
                              loading_point_id=2,
                              unloading_point_id=1)
        self.assertTrue(result)  # валидируем результат (result == True)

    def test_get_robot(self):
        """ Тест функции поиска записи Robot по id пункта загрузки """
        result = get_robot_by_loading_point(self.session, load_p_id=1)
        self.assertIsNotNone(result)  # запись должна существовать
        self.assertTrue(result.loading_point_id == 1)


    def test_delete_robot(self):
        """Тест функции удаления записи робота по id пункта загрузки"""
        delete_robot_by_loading_point(self.session, load_p_id=2)
        result = get_robot_by_loading_point(self.session, load_p_id=2)
        self.assertIsNone(result)  # запись не должна существовать

    def test_update_robot_charge(self):
        """Тест функции обновления заряда робота по id пункта загрузки"""
        update_robot_charge(self.session, _charge=60, load_p_id=1)

    def tearDown(self):
        """ Наследуемый метод tearDown определяет инструкции,
            которые должны быть выполнены ПОСЛЕ тестирования """
        self.session.close()  # закрываем соединение с БД


if __name__ == '__main__':
    unittest.main()
