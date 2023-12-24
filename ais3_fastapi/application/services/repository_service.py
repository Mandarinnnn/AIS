from typing import Optional, Iterable
from sqlalchemy.orm import Session
from application.models.dao import *
import functools
import traceback

"""

    Данный модуль является промежуточным слоем приложения, который отделяет операции 
    для работы с моделями DAO от основной бизнес-логики приложения. Создание данного 
    слоя позволяет унифицировать функции работы с источником данных, и, например, если 
    в приложении нужно будет использовать другой framework для работы с БД, вы можете 
    создать новый модуль (newframework_repository_service.py) и реализовать в нем функции 
    с аналогичными названиями (get_weather_by_city_id, и т.д.). Новый модуль можно будет
    просто импортировать в модуль с основной бизнес-логикой, практически не меняя при этом
    остальной код.
    Также отделение функций работы с БД можно сделать через отдельный абстрактный класс и 
    использовать порождающий паттерн для переключения между необходимыми реализациями.

"""


def dbexception(db_func):
    """ Функция-декоратор для перехвата исключений БД.
        Данный декоратор можно использовать перед любыми
        функциями, работающими с БД, чтобы не повторять в
        теле функции конструкцию try-except (как в функции add_weather). """

    @functools.wraps(db_func)
    def decorated_func(db: Session, *args, **kwargs) -> bool:
        try:
            db_func(db, *args, **kwargs)  # вызов основной ("оборачиваемой") функции
            db.commit()  # подтверждение изменений в БД
            return True
        except Exception as ex:
            # выводим исключение и "откатываем" изменения
            print(f'Exception in {db_func.__name__}: {traceback.format_exc()}')
            db.rollback()
            return False

    return decorated_func


def create_robot(db: Session, charge: int, position_x: int, position_y: int, r_state: int, loading_point_id: int, unloading_point_id: int) -> bool:
    robot = RobotLoader(
        charge=charge,
        position_x=position_x,
        position_y=position_y,
        r_state=r_state,
        loading_point_id=loading_point_id,
        unloading_point_id=unloading_point_id
    )

    return add_robot(db, robot)


@dbexception
def add_robot(db: Session, robot: RobotLoader) -> bool:
    try:
        db.add(robot)
        print(robot)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


def create_loading_point(db: Session, position_x: int, position_y: int, status: int) -> bool:
    loading_point = LoadingPoints(
        position_x=position_x,
        position_y=position_y,
        status=status
    )

    return add_loading_point(db, loading_point)


@dbexception
def add_loading_point(db: Session, loading_point: LoadingPoints) -> bool:
    try:
        db.add(loading_point)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


def create_unloading_point(db: Session, position_x: int, position_y: int, status: int) -> bool:
    unloading_point = UnloadingPoints(
        position_x=position_x,
        position_y=position_y,
        status=status
    )
    return add_unloading_point(db, unloading_point)


@dbexception
def add_unloading_point(db: Session, unloading_point: UnloadingPoints) -> bool:
    try:
        db.add(unloading_point)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


def get_robot_by_loading_point(db: Session, load_p_id: int) -> Optional[RobotLoader]:
    result = db.query(RobotLoader).filter(RobotLoader.loading_point_id == load_p_id).first()
    return result

def get_robot_by_id(db: Session, id: int) -> Optional[RobotLoader]:
    result = db.query(RobotLoader).filter(RobotLoader.id == id).first()
    print(result)
    return result


def get_robot_by_unloading_point(db: Session, unload_p_id: int) -> Optional[RobotLoader]:
    result = db.query(RobotLoader).filter(RobotLoader.loading_point_id == unload_p_id).all()
    return result



def get_robot_by_position(db: Session, pos_x1: int, pos_x2: int, pos_y1: int, pos_y2: int) -> Optional[RobotLoader]:
    result = db.query(RobotLoader).filter(RobotLoader.position_x >= pos_x1).all()
    """and
                                          RobotLoader.position_x <= pos_x2 and
                                          RobotLoader.position_y >= pos_y1 and
                                          RobotLoader.position_y <= pos_y2).all()
"""


def get_all_robots(db: Session):
    result = db.query(RobotLoader).all()
    return result


def update_robot_position(db: Session, pos_x: int, pos_y: int, load_p_id: int) -> bool:
    robot = get_robot_by_loading_point(db, load_p_id)
    robot.position_x = pos_x
    robot.position_y = pos_y
    return add_robot(db, robot)


def update_robot_charge(db: Session, _charge: int, load_p_id: int) -> bool:
    robot = get_robot_by_loading_point(db, load_p_id)
    robot.charge = _charge
    return add_robot(db, robot)

def update_robot_state(db: Session, state: int, id: int) -> bool:
    robot = get_robot_by_id(db, id)
    robot.r_state = state
    return add_robot(db, robot)


@dbexception
def delete_robot_by_loading_point(db: Session, load_p_id: int) -> bool:
    robot = get_robot_by_loading_point(db, load_p_id)
    db.delete(robot)


def create_state(db: Session, _state: str) -> bool:
    r_state = RobotStates(
        state=_state
    )
    add_state(db, r_state)


@dbexception
def add_state(db: Session, state: RobotStates):
    try:
        db.add(state)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True


def create_status(db: Session, _status: str) -> bool:
    p_status = PointStatuses(
        status=_status
    )
    add_status(db, p_status)


def add_status(db: Session, status: PointStatuses):
    try:
        db.add(status)
        db.commit()
    except Exception as ex:
        print(traceback.format_exc())
        db.rollback()
        return False
    return True
