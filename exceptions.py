"""exception module"""

class GameOver(Exception):
    """finishes the game"""
    @classmethod
    def write_score(cls, gm_score, gm_name):
        with open("score.txt", "a") as file:
            file.write(gm_name + " -" " Очков: " + str(gm_score) + "\n")


class EnemyDown(Exception):
    pass
