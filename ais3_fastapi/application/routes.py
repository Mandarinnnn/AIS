from fastapi import APIRouter, HTTPException, status, Request, Response
from starlette.responses import RedirectResponse
from application.models.dto import *
from application.services.robot_service import RobotService


"""

    Данный модуль отвечает за маршрутизацию доступных API URI (endpoints) сервера

"""


router = APIRouter(prefix='/api', tags=['RobotLoader API'])       # подключаем данный роутер к корневому адресу /api
service = RobotService()              # подключаем слой с дополнительной бизнес-логикой


@router.get('/')
async def root():
    """ Переадресация на страницу Swagger """
    return RedirectResponse(url='/docs', status_code=307)


@router.get('/robotloader', response_model=RobotDTO)
async def get_robot_by_id(id: int):
    """ Получение записи о роботе по идентификатору (необходим параметр ?id=) """
    response = service.get_robot_by_id(id)
    if response is None:
        return Response(status_code=204)
    return response


@router.get('/robotloader/', response_model=List[RobotDTO])
async def get_all_robots():
    """ Получение всех записей о роботах """
    return service.get_all_robots()


@router.post('/robotloader', status_code=201)
async def post_robotloader(robot: RobotDTO):
    """ Добавить новую запись о роботе """
    if service.add_robot(robot):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new Robot data",
        )



@router.put('/robotloader', status_code=202)
async def put_robotloader_state(robot: RobotDTO):
    """ Обновить режим работы робота """
    if service.update_robot_state(robot):
        return Response(status_code=202)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't update Robot data",
        )



@router.delete('/robotloader/{load_p_id}', status_code=200)
async def del_robotloader(load_p_id: str):
    """ Удаление записи о роботе по id пункта загрузки """
    if service.delete_robot_by_loading_point(load_p_id):
        return Response(status_code=200)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't delete Robot data",
        )

@router.post('/loading_point', status_code=201)
async def create_loading_point(load_p: LoadingPointDTO) -> Response:
    """ Добавить новый пункт загрузки """
    if service.add_loading_point(load_p):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new Loading Point data",
        )


@router.post('/unloading_point', status_code=201)
async def create_unloading_point(unload_p: UnloadingPointDTO) -> Response:
    """ Добавить новый пункт разгрузки """
    if service.add_unloading_point(unload_p):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new Unloading Point data",
        )

@router.post('/robotloader', status_code=201)
async def create_robot(robot: RobotDTO) -> Response:
    """ Добавить робота """
    if service.add_robot(robot):
        return Response(status_code=201)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Can't add new Loading Point data",
        )
