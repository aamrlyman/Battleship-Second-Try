from gameboard import Gameboard
from enum import Enum


class Player:
    def __init__(self) -> None:
        self.name = input("Type your name here: ")
        self.gameboard = Gameboard()
        self.total_hitpoints:int = 0

    def choose_y_coordinate(self):
        Y_coord = input("Choose a letter between A_J:")
        print(Y[Y_coord.upper()])
    
    def place_ships(self):
        pass

