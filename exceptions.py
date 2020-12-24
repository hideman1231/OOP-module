class GameOver(Exception):
    @classmethod
    def write_score(cls, gm_score, gm_name):
        with open("score.txt", "a") as f:
            f.write(gm_name + " -" " Очков: " + str(gm_score) + "\n")


class EnemyDown(Exception):
    pass
