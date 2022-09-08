from player import Player

class Game: 
    def __init__(self) -> None:
        self.players:list[object] = [Player(), Player()]


    def game_intro(self):
        pass

    def update(self, player)
        display_fleet_status(player)
        print(player.total_health)
        display_attack_log(player)

    def attack(self, player):
        pass


    def attack_phase(self, player_1: object, player_2:object):
        player_1 = self.players[0]
        player_2 = self.players[1]
        while player_1.total_hitpoints > 0 and player_2.total_hitpoints > 0:
            for player in players:
                update(player)
                attack(player)
                

    def declare_winner:
        winner = player_1 if player_1.total_hitpoints > player_2.total_hitpoints else player_2
        for player in self.players:
            display_fleet_status(player)
        print(f'{winner} is the winner!)




