"""all logic"""
import random


from exceptions import GameOver, EnemyDown


class Enemy:
    """Creates enemy"""
    def __init__(self, level: int, lives: int):
        self.level = level
        self.lives = lives

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        print("Enemy HP:", self.lives)
        if self.lives == 0:
            raise EnemyDown


class Player:
    """Creates player"""
    def __init__(self, name: str, lives: int, score: int, allowed_attacks: int):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        if attack == defense:
            return 0
        elif attack == 1 and defense == 3:
            return -1
        elif attack == 2 and defense == 1:
            return -1
        elif attack == 3 and defense == 2:
            return -1
        else:
            return 1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def attack(self, enemy_obj):
        self.fight(self.allowed_attacks, enemy_obj.select_attack())
        if self.fight(self.allowed_attacks, enemy_obj.select_attack()) == 0:
            print("Attack: It's a draw!")
        elif self.fight(self.allowed_attacks, enemy_obj.select_attack()) == 1:
            print("Attack: You attacked successfully!")
            enemy_obj.decrease_lives()
        else:
            print("Attack: You missed!")

    def defence(self, enemy_obj):
        self.fight(enemy_obj.select_attack(), self.allowed_attacks)
        if self.fight(enemy_obj.select_attack(), self.allowed_attacks) == 0:
            print("Defence: It's a draw!")
        elif self.fight(enemy_obj.select_attack(), self.allowed_attacks) == 1:
            print("Defence: You missed!")
            self.decrease_lives()
        else:
            print("Defence: You attacked successfully!")
            self.score += 1

    @classmethod
    def validate_names(cls, names):
        with open("score.txt", "r") as file:
            for i in file.readlines():
                if names in i.split()[0]:
                    return False

    def validate_allowed_attacks(self):
        if self.allowed_attacks not in [1,2,3]:
            return False


class Score:
    """Shows the top ten players by score"""
    @classmethod
    def player_top(cls):
        with open("score.txt", "r") as file:
            lines = file.readlines()
            lines.sort(key=lambda x: int(x.split()[-1]), reverse=True)
        for i in lines[:10]:
            print(i.strip())
