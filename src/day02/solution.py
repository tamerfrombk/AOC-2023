from dataclasses import dataclass
from utils import sumlines, product


@dataclass
class Game:
    gid: int
    hands: list[dict[str, int]]

    def is_possible(self) -> bool:
        return all(
            hand["red"] <= 12 and hand["green"] <= 13 and hand["blue"] <= 14
            for hand in self.hands
        )

    @property
    def fewest_cubes(self) -> dict[str, int]:
        fewest = {"red": 0, "green": 0, "blue": 0}
        for hand in self.hands:
            for color in ["red", "green", "blue"]:
                fewest[color] = max(fewest[color], hand[color])

        return fewest

    def power(self) -> int:
        return product(self.fewest_cubes.values())


# Game 1: 9 red, 5 blue, 6 green; 6 red, 13 blue; 2 blue, 7 green, 5 red
def parse_game(line: str) -> Game:
    game, handfuls = line.split(":")
    gid = int(game.split(" ")[1].strip())
    handfuls = [hand.split(",") for hand in handfuls.split(";")]

    hands = []
    for handful in handfuls:
        cubes = [cube.split(" ") for cube in handful]
        hand = {"red": 0, "green": 0, "blue": 0}
        for cube in cubes:
            assert cube[0] == ""
            count = int(cube[1].strip())
            color = cube[2].strip()
            hand[color] = count
        hands.append(hand)

    return Game(gid, hands)


def solve1(input: str) -> int:
    return sumlines(
        input,
        parser=parse_game,
        filter_fn=Game.is_possible,
        transformer=lambda game: game.gid,
    )


def solve2(input: str) -> int:
    return sumlines(input, parser=parse_game, transformer=Game.power)
