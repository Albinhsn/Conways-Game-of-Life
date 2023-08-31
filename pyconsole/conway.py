import time
from typing import Tuple

from shapes import *


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
    return check_dead(possible_blocks, blocks) + check_alive(blocks, blocks)


def print_blocks(blocks):
    min_x = min([i[0] for i in blocks])
    max_x = max([i[0] for i in blocks])

    min_y = min([i[1] for i in blocks])
    max_y = max([i[1] for i in blocks])
    max_xy = max(max_x, max_y)
    min_xy = min(min_x, min_y)
    print("-" * 50)
    for j in range(min_y, max_y + 1):
        print("\t")
        for i in range(min_x, max_x + 1):
            if (i, j) in blocks:
                print(" x ", end="")
            else:
                print("   ", end="")
        print()


def main() -> int:
    blocks = space_ship()
    print_blocks(blocks)
    while True:
        blocks = cycle(blocks)
        print_blocks(blocks)
        time.sleep(0.75)


if __name__ == "__main__":
    exit(main())
