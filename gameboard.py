from ship import Ship
from enum import Enum
from coordinates import C

class Y(Enum): #Y axis enum class
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
        self.spaces = [
            [C({Y.A:1}), C({Y.A:2}),C({Y.A:3}), C({Y.A:4}), C({Y.A:5}), C({Y.A:6}), C({Y.A:7}), C({Y.A:8}), C({Y.A:9}), C({Y.A:10})], 
            [C({Y.B:1}), C({Y.B:2}),C({Y.B:3}), C({Y.B:4}), C({Y.B:5}), C({Y.B:6}), C({Y.B:7}), C({Y.B:8}), C({Y.B:9}), C({Y.B:10})], 
            [C({Y.C:1}), C({Y.C:2}),C({Y.C:3}), C({Y.C:4}), C({Y.C:5}), C({Y.C:6}), C({Y.C:7}), C({Y.C:8}), C({Y.C:9}), C({Y.C:10})], 
            [C({Y.D:1}), C({Y.D:2}),C({Y.D:3}), C({Y.D:4}), C({Y.D:5}), C({Y.D:6}), C({Y.D:7}), C({Y.D:8}), C({Y.D:9}), C({Y.D:10})], 
            [C({Y.E:1}), C({Y.E:2}),C({Y.E:3}), C({Y.E:4}), C({Y.E:5}), C({Y.E:6}), C({Y.E:7}), C({Y.E:8}), C({Y.E:9}), C({Y.E:10})], 
            [C({Y.F:1}), C({Y.F:2}),C({Y.F:3}), C({Y.F:4}), C({Y.F:5}), C({Y.F:6}), C({Y.F:7}), C({Y.F:8}), C({Y.F:9}), C({Y.F:10})], 
            [C({Y.G:1}), C({Y.G:2}),C({Y.G:3}), C({Y.G:4}), C({Y.G:5}), C({Y.G:6}), C({Y.G:7}), C({Y.G:8}), C({Y.G:9}), C({Y.G:10})], 
            [C({Y.H:1}), C({Y.H:2}),C({Y.H:3}), C({Y.H:4}), C({Y.H:5}), C({Y.H:6}), C({Y.H:7}), C({Y.H:8}), C({Y.H:9}), C({Y.H:10})], 
            [C({Y.I:1}), C({Y.I:2}),C({Y.I:3}), C({Y.I:4}), C({Y.I:5}), C({Y.I:6}), C({Y.I:7}), C({Y.I:8}), C({Y.I:9}), C({Y.I:10})], 
            [C({Y.J:1}), C({Y.J:2}),C({Y.J:3}), C({Y.J:4}), C({Y.J:5}), C({Y.J:6}), C({Y.J:7}), C({Y.J:8}), C({Y.J:9}), C({Y.J:10})], 
         
        ] 
            

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

 

    
