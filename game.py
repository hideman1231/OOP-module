"""main executable"""
from exceptions import GameOver, EnemyDown
from models import Player, Enemy, Score
import settings

player_list = [0]



def play():
    while True:
        command = input("What you want to do? START, SHOW, HELP, TOP, EXIT: ")
        if command == "START":
            next_lvl = 1
            names = input("Enter your name: ")	
            print()
            while Player.validate_names(names) is False:
                print("Name already exists")
                names = input("Enter your name: ")
            player = Player(names, settings.LIVES, 0, 0)
            enemy = Enemy(1, 1)
            while True:
                try:
                    while True:
                        player.allowed_attacks = int(input("Choose your hero: 1-Wizard, 2-Warrior, 3-Rogue "))
                        if player.validate_allowed_attacks() is False:
                            print("The selected hero does not exist")
                            continue
                        else:
                            player.attack(enemy)
                            break
                    while True:
                        player.allowed_attacks = int(input("Choose defense: 1-Wizard, 2-Warrior, 3-Rogue "))
                        if player.validate_allowed_attacks() is False:
                            print("The selected hero does not exist")
                            continue
                        else:
                            player.defence(enemy)
                            break
                except EnemyDown:
                    next_lvl += 1
                    print("------------------------------------")
                    print("You killed enemy!", "Score:", player.score, "Level:", enemy.level)
                    print("------------------------------------")
                    enemy = Enemy(enemy.level+next_lvl, enemy.lives+next_lvl)
                    player.score += 5
                player_list.append(player)
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
        GameOver.write_score(player_list[-1].score, player_list[-1].name)
    except KeyboardInterrupt:
        pass
    finally:
        print()
        print("Good bye!")
