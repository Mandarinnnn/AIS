from pydantic import BaseModel


class LoadingPointDTO(BaseModel):
    """ DTO для добавления нового пункта загрузки """
    position_x: int
    position_y: int
    status: int


class UnloadingPointDTO(BaseModel):
    """ DTO для добавления нового пункта разгрузки """
    position_x: int
    position_y: int
    status: int
