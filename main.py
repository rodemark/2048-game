from Drawing import Drawing
from GameField import GameField


def main():
    gameField = GameField(4)
    gameField.spawn_tile()
    gameField.spawn_tile()
    drawer = Drawing(gameField)
    drawer.run_game()


if __name__ == "__main__":
    main()