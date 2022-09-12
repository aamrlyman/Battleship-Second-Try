from enum import Enum


class Status(Enum):
    blank = 1
    ship = 2
    miss = 3
    hit = 5

class Square: #coordinate class
    def __init__(self, coordinate: object) -> None:
        self.coordinate = coordinate
        self.status = Status.blank


        