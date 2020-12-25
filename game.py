"""main executable"""
from exceptions import GameOver, EnemyDown
from models import Player, Enemy, Score
import settings

score_list = [0]
name_list = []



def play():
    while True:
        command = input("What you want to do? START, SHOW, HELP, TOP, EXIT: ")
        if command == "START":
            next_lvl = 1
            names = input("Enter your name: ")	
            print()
            while True:
                if Player.validate_names(names) == 0:
                    print("Name already exists")
                    names = input("Enter your name: ")
                else:
                    player = Player(names, settings.LIVES, 0, 0)
                    break
            enemy = Enemy(1, 1)
            while True:
                try:
                    player.allowed_attacks = int(input("Choose your hero: 1-Wizard, 2-Warrior, 3-Rogue "))
                    if player.validate_allowed_attacks() == 0:
                        print("The selected hero does not exist")
                        player.allowed_attacks = int(input("Choose your hero: 1-Wizard, 2-Warrior, 3-Rogue "))
                    else:
                        player.attack(enemy)
                        player.allowed_attacks = int(input("Choose defense: 1-Wizard, 2-Warrior, 3-Rogue "))
                    if player.validate_allowed_attacks() == 0:
                        print("The selected hero does not exist")
                        player.allowed_attacks = int(input("Choose defense: 1-Wizard, 2-Warrior, 3-Rogue "))
                    else:
                        player.defence(enemy)
                except EnemyDown:
                    next_lvl += 1
                    print("------------------------------------")
                    print("You killed enemy!", "Score:", player.score, "Level:", enemy.level)
                    print("------------------------------------")
                    enemy = Enemy(enemy.level+next_lvl, enemy.lives+next_lvl)
                    player.score += 5
                score_list.append(player.score)
                name_list.append(player.name)
        if command == "SHOW":
            with open("score.txt", "r") as file:
                print(file.read())
        if command == "HELP":
            print("All commands:", ",".join(settings.HELP))
        if command == "TOP":
            Score.player_top()
        if command == "EXIT":
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        GameOver.write_score(score_list[-1], name_list[-1])
    except KeyboardInterrupt:
        pass
    finally:
        print()
        print("Good bye!")
