import time
from typing import Tuple


def get_possible(blocks):
    XY = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    new_blocks = set()
    for block in blocks:
        for xy in XY:
            new_block = (block[0] + xy[0], block[1] + xy[1])
            if new_block not in blocks:
                new_blocks.add(new_block)

    return list(new_blocks)


def get_neighbours(block, blocks) -> int:
    XY = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    cnt = 0
    for xy in XY:
        if (block[0] + xy[0], block[1] + xy[1]) in blocks:
            cnt += 1
    return cnt


def check_dead(possible_blocks, blocks) -> list[Tuple[int, int]]:
    return [i for i in possible_blocks if get_neighbours(i, blocks) == 3]


def check_alive(possible_blocks, blocks) -> list[Tuple[int, int]]:
    return [i for i in possible_blocks if get_neighbours(i, blocks) in [2, 3]]


def cycle(blocks):
    possible_blocks = get_possible(blocks)
    dead = check_dead(possible_blocks, blocks)
    alive = check_alive(blocks, blocks)
    print(dead)
    print(alive)
    return dead + alive


def get_stick():
    return [(0, 0), (0, -1), (0, -2)]


def sailor():
    return [(0, 0), (1, 0), (0, -1), (-1, 1), (-1, -1)]


def space_ship():
    return [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (3, -1),
        (3, -2),
        (2, -3),
        (-1, -1),
        (-1, -3),
    ]


def pulse():
    return [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, -2),
        (3, -3),
        (3, -4),
        (2, -5),
        (1, -5),
        (0, -5),
        (-2, -2),
        (-2, -3),
        (-2, -4),
        # snd one
        (0, -7),
        (1, -7),
        (2, -7),
        (3, -8),
        (3, -9),
        (3, -10),
        (-2, -8),
        (-2, -9),
        (-2, -10),
        (0, -12),
        (1, -12),
        (2, -12),
        # third one
        (5, -2),
        (5, -3),
        (5, -4),
        (6, -5),
        (7, -5),
        (8, -5),
        (6, 0),
        (7, 0),
        (8, 0),
        (10, -2),
        (10, -3),
        (10, -4),
    ]


def print_blocks(blocks):
    min_x = min([i[0] for i in blocks])
    max_x = max([i[0] for i in blocks])

    min_y = min([i[1] for i in blocks])
    max_y = max([i[1] for i in blocks])
    max_xy = max(max_x, max_y)
    min_xy = min(min_x, min_y)
    print("-" * 15)
    for j in range(min_xy, max_xy+1):
        print("\t")
        for i in range(min_xy, max_xy+4):
            if (i, j) in blocks:
                print("[x]", end="")
            else:
                print("[ ]", end="")
        print()


def main() -> int:
    blocks = pulse()
    print_blocks(blocks)
    exit()
    while True:
        blocks = cycle(blocks)
        print_blocks(blocks)
        time.sleep(0.75)
    return 0


if __name__ == "__main__":
    exit(main())
