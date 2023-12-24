from application.config import SessionLocal
from application.services.repository_service import *
import random
import pymysql
""" Данный скрипт заполняет БД тестовыми данными """


CITY = ['UFA', 'MOSCOW', 'SAINT-PETERSBURG']

WEATHER_TYPE = ['CLEAN', 'CLOUDY', 'RAIN']




if __name__ == "__main__":
    with SessionLocal() as session:
        create_state(session,"Стоит")
        create_state(session,"Движется")
        create_status(session,"Свободен")
        create_status(session,"Занят")
        create_loading_point(session,random.randint(1,50),random.randint(1,50),status=1)
        create_loading_point(session,random.randint(1,50),random.randint(1,50),status=1)
        create_unloading_point(session,random.randint(1,50),random.randint(1,50),status=1)
        create_robot(session,random.randint(90,100),random.randint(1,50),
                     random.randint(1,50),r_state=1,loading_point_id=1,unloading_point_id=1)
