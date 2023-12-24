from sqlalchemy import Column, ForeignKey, Boolean, Integer, Numeric, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from datetime import datetime


# Объявление декларативного (описательного) метода представления БД
Base = declarative_base()


class RobotStates(Base):
    __tablename__ = "robot_states"

    id = Column(Integer, primary_key=True)      # Первичный ключ - id
    state = Column(String(255), nullable=False)        # Состояние робота


class PointStatuses(Base):
    __tablename__ = "point_statuses"

    id = Column(Integer, primary_key=True)      # Первичный ключ - id
    status = Column(String(255), nullable=False)        # Статус пункта


class LoadingPoints(Base):
    __tablename__ = "loading_points"

    id = Column(Integer, primary_key=True)  # Первичный ключ - id
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    status = Column(Integer, ForeignKey('point_statuses.id'), nullable=False)
    status_name = relationship('PointStatuses')


class UnloadingPoints(Base):
    __tablename__ = "unloading_points"

    id = Column(Integer, primary_key=True)  # Первичный ключ - id
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    status = Column(Integer, ForeignKey('point_statuses.id'), nullable=False)
    status_name = relationship('PointStatuses')


class RobotLoader(Base):
    __tablename__ = "robot_loader"
    id = Column(Integer, primary_key=True)  # Первичный ключ - id
    charge = Column(Integer, nullable=False)
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    r_state = Column(Integer, ForeignKey('robot_states.id'))
    state_name = relationship('RobotStates')
    loading_point_id = Column(Integer, ForeignKey('loading_points.id'),unique=True)
    loading_point = relationship('LoadingPoints')
    unloading_point_id = Column(Integer, ForeignKey('unloading_points.id'))
    unloading_point = relationship('UnloadingPoints')


    def __repr__(self):
        """ Переопределяем строковое представление объекта (см. python magic methods)"""
        return f'{self.__dict__}'
