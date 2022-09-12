from coordinates import Square


class Ship:
    def __init__(self, name , hitpoints: int) -> None:
        self.name = name
        self.hitpoints = hitpoints
        self.position: list[Square] = []