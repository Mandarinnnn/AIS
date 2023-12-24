from typing import Optional, List
from application.config import SessionLocal
from application.models.dao import RobotLoader
from application.models.dto import RobotDTO, LoadingPointDTO, UnloadingPointDTO
import application.services.repository_service as repository_service


"""

    Данный модуль содержит программный слой с реализацией дополнительной бизнес-логики, 
    выполняемой перед или после выполнения операций над хранилищем данных (repository), 
    например: маппинг атрибутов из DAO в DTO, применение дополнительных функций к атрибутам DTO.
    
    ВАЖНО! Реализация данного слоя приведена в качестве демонстрации полной структуры RESTful веб-сервиса.
           В небольших проектах данный слой может быть избыточен, в таком случае, из контроллера ваших маршрутов 
           (Router в FastAPI или View в Django) можно напрямую работать с функциями хранилища данных (repository_service).

"""


class RobotService:

    def get_robot_by_loading_point(self,load_p_id: int) -> Optional[RobotDTO]:
        result = None
        with SessionLocal() as session:
            result = repository_service.get_robot_by_loading_point(session, load_p_id)
        if result is not None:
            return self.map_robot_data_to_dto(result)
        return result

    def get_robot_by_id(self, id: int) -> Optional[RobotDTO]:
        result = None
        with SessionLocal() as session:
            result = repository_service.get_robot_by_id(session, id)
        if result is not None:
            return self.map_robot_data_to_dto(result)
        return result






    def get_all_robots(self) -> List[RobotDTO]:
        robot_data: List[RobotDTO] = []
        with SessionLocal() as session:
            result = repository_service.get_all_robots(session)
            for rob in result:
                robot_data.append(self.map_robot_data_to_dto(rob))
        return robot_data

    def add_loading_point(self, load_p: LoadingPointDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.create_loading_point(session,
                                                           position_x=load_p.position_x,
                                                           position_y=load_p.position_y,
                                                           status=load_p.status)

    def add_unloading_point(self, unload_p: UnloadingPointDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.create_unloading_point(session,
                                                             position_x=unload_p.position_x,
                                                             position_y=unload_p.position_y,
                                                             status=unload_p.status)

    def add_robot(self, robot: RobotDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.create_robot(session,
                                                   charge=robot.charge,
                                                   position_x=robot.position_x,
                                                   position_y=robot.position_y,
                                                   r_state=robot.r_state,
                                                   loading_point_id=robot.loading_point_id,
                                                   unloading_point_id=robot.unloading_point_id)



    def update_robot_charge(self, robot: RobotDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.update_robot_charge(session,_charge=robot.charge,load_p_id=robot.loading_point_id)


    def update_robot_state(self, robot: RobotDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.update_robot_state(session,state=robot.r_state,id=robot.id)


    def update_robot_position(self, robot: RobotDTO) -> bool:
        with SessionLocal() as session:
            return repository_service.update_robot_position(session,
                                                            charge=robot.charge,
                                                            position_x=robot.position_x,
                                                            position_y=robot.position_y,
                                                            r_state=robot.r_state,
                                                            loading_point_id=robot.loading_point_id,
                                                            unloading_point_id=robot.unloading_point_id)

    def delete_robot_by_loading_point(self, load_p_id: int) -> bool:
        with SessionLocal() as session:
            return repository_service.delete_robot_by_loading_point(session, load_p_id)

    """ Метод для конвертирования (маппинга) Weather DAO в WeatherDTO """


    def map_robot_data_to_dto(self, robot_dao: RobotLoader):
        """ Метод для конвертирования (маппинга) Robot DAO в RobotDTO """
        return RobotDTO(id=robot_dao.id,
                        charge=robot_dao.charge,
                        position_x=robot_dao.position_x,
                        position_y=robot_dao.position_y,
                        r_state=robot_dao.r_state,
                        loading_point_id=robot_dao.loading_point_id,
                        unloading_point_id=robot_dao.unloading_point_id)
