from tkinter import Y
from ship import Ship
from enum import Enum

class Y_Axis(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10

class ship_names(Enum):
    Destroyer = 1
    Submarine = 2
    Battleship = 3
    Aircraft_Carrier = 4

class Gameboard: 
    def __init__(self) -> None:
        self.spaces = [[Y_Axis.A, Y_Axis.B, Y_Axis.C, Y_Axis.D, Y_Axis.E, 
                     Y_Axis.F, Y_Axis.G, Y_Axis.H, Y_Axis.I, Y_Axis.J], 
                     1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
        self.fleet = [
            Ship(ship_names.Aircraft_Carrier, 5), 
            Ship(ship_names.Battleship, 4), 
            Ship(ship_names.Submarine, 3),
            Ship(ship_names.Destroyer, 2)
             ]

        self.Attacked_coordinates: list[object] = []
        
    def display_fleet_status(self):
        pass    

    def display_attack_log(self):
        pass

 

    
