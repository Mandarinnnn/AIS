from pydantic import BaseModel
from typing import (
    Deque, Dict, List, Optional, Sequence, Set, Tuple, Union
)

from datetime import datetime


class RobotDTO(BaseModel):
    id: int
    charge: int
    position_x: int
    position_y: int
    r_state: int
    loading_point_id: int
    unloading_point_id: int

