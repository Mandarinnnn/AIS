import json
import time
import random
import json
from locust import HttpUser, task, tag, between


# Статичные данные для тестирования
CITY_NAMES = ['ufa', 'moscow', 'saint-petersburg', 'kazan']

WEATHER_TYPES = ['CLEAN', 'CLOUDY', 'RAIN']


class RESTServerUser(HttpUser):
    """ Класс, эмулирующий пользователя / клиента сервера """
    wait_time = between(1.0, 5.0)       # время ожидания пользователя перед выполнением новой task

    # Адрес, к которому клиенты (предположительно) обращаются в первую очередь (это может быть индексная страница, страница авторизации и т.п.)
    def on_start(self):
        self.client.get("/docs")    # базовый класс HttpUser имеет встроенный HTTP-клиент для выполнения запросов (self.client)




    @tag("get_one_task")
    @task(1)
    def get_one_task(self):
        """ Тест GET-запроса (получение данных о роботе)"""
        load_p_id = random.randint(1,3)
        with self.client.get(f'/api/robotloader?id={load_p_id}',
                             catch_response=True,
                             name= f'/api/robotloader?id={load_p_id}') as response:
            if response.status_code == 200:
                response.success()
                # Иначе обозначаем как "отказ"
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("put_task")
    @task(3)
    def put_task(self):
        """ Тест PUT-запроса (обновление записи о зарядке робота) """
        city_id = random.randint(0, 3)  # генерируем случайный id в диапазоне [0, 3]
        city_name = CITY_NAMES[city_id]  # получаем случайное значение населенного пункта из списка CITY_NAMES

        load_p_id = random.randint(1, 2)
        test_data = {'charge': random.randint(40, 80),
                     "position_x": 10,
                     "position_y": 10,
                     "r_state": 1,
                     "loading_point_id": load_p_id,
                     "unloading_point_id": 1
                     }


        put_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/weatherforecast/{city_name}
        with self.client.put('/api/robotloader',
                             catch_response=True,
                             name='/api/robotloader',
                             data=put_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 202:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("post_task")
    @task(1)
    def post_task(self):
        """Тест POST - запроса (создание записи о пункте разгрузки)"""
        # Генерируем случайные данные в опредленном диапазоне
        test_data = {  "position_x": random.randint(1,100), "position_y": random.randint(1,100), "status": 1 }
        post_data = json.dumps(test_data)  # сериализуем тестовые данные в json-строку
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/api/weatherforecast
        with self.client.post('/api/unloading_point',
                              catch_response=True,
                              name='/api/unloading_point', data=post_data,
                              headers={'content-type': 'application/json'}) as response:
            # проверяем, корректность возвращаемого HTTP-кода
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')


    @tag("put_task_mode")
    @task(1)
    def put_task_mode(self):
        """ Тест PUT-запроса (обновление записи о режиме работы робота) """
        mode = random.randint(1, 3)  # генерируем случайный id в диапазоне [0, 3]

        test_data = {"id": 1,
                     'charge': 1,
                     "position_x": 10,
                     "position_y": 10,
                     "r_state": mode,
                     "loading_point_id": 1,
                     "unloading_point_id": 1
                     }


        put_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/weatherforecast/{city_name}
        with self.client.put('/api/robotloader',
                             catch_response=True,
                             name='/api/robotloader',
                             data=put_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 202:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

