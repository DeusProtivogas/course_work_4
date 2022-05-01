from dataclasses import dataclass
from functools import wraps

from data.units.BaseUnit import BaseUnit
from data.units.Enemy import Enemy
from data.units.Player import Player



@dataclass
class Arena():
    recovery: float
    player: Player
    enemy: Enemy
    game_is_on: bool
    game_results = ""

    def __init__(self):
        self.player = None
        self.enemy = None
        self.game_is_on = False


    def game_start(self, player, enemy):
        self.game_is_on = True
        self.player = player
        self.enemy = enemy

    def game_over(self, results: str):
        self.game_is_on = False
        self.game_results = results
        return results

    def stamina_regen(self):
        self.player.regenerate_stamina()
        self.enemy.regenerate_stamina()

    def health_check(self):
        if self.enemy.hit_points <= 0 and self.player.hit_points <= 0:
            return self.game_over(results="Ничья")
        if self.enemy.hit_points <= 0:
            return self.game_over(results="Игрок победил")
        if self.player.hit_points <= 0:
            return self.game_over(results="Игрок проиграл")
        return None

    def next_turn(self) -> str:
        result = self.health_check()
        if result:
            return result

        if not self.game_is_on:
            return self.game_results

        self.stamina_regen()

        enemy_attack_results = self.enemy.hit(self.player)

        return enemy_attack_results

    def player_hit(self) -> str:
        player_res = f"{self.player.hit(target=self.enemy)}"
        enemy_res = f"{self.next_turn()}"

        return f"<p>{player_res}</p><p>{enemy_res}</p>"

    def player_skill(self) -> str:
        player_res = f"<p> {self.player.use_skill(target=self.enemy)} </p>"
        enemy_res = f"<p> {self.next_turn()} </p>"

        return f"{player_res} {enemy_res}"


