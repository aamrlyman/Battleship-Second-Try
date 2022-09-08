from gameboard import Gameboard


class Player:
    def __init__(self) -> None:
        self.name = input("Type your name here: ")
        self.gameboard = Gameboard()
        self.total_hitpoints:int = 0

    def place_ships(self):
        pass

