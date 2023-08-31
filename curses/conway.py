import curses
import time
from typing import Tuple

from shapes import get_stick, space_ship


def get_pos(h, w):
    return [(w + i[0], h + i[1]) for i in space_ship()]


def get_neighbours(block, blocks) -> int:
    XY = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
    cnt = 0
    for xy in XY:
        if (block[0] + xy[0], block[1] + xy[1]) in blocks:
            cnt += 1
    return cnt


def get_possible(blocks):
    XY = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    new_blocks = set()
    for block in blocks:
        for xy in XY:
            new_block = (block[0] + xy[0], block[1] + xy[1])
            if new_block not in blocks:
                new_blocks.add(new_block)

    return list(new_blocks)


def check_dead(possible_blocks, blocks) -> list[Tuple[int, int]]:
    return [i for i in possible_blocks if get_neighbours(i, blocks) == 3]


def check_alive(possible_blocks, blocks) -> list[Tuple[int, int]]:
    return [i for i in possible_blocks if get_neighbours(i, blocks) in [2, 3]]


def cycle(blocks):
    possible_blocks = get_possible(blocks)
    return check_dead(possible_blocks, blocks) + check_alive(blocks, blocks)


def paint_blocks(stdscr, blocks, string):
    for s in blocks:
        stdscr.addstr(s[1], s[0], string)
    stdscr.refresh()


def main(stdscr):
    stdscr.clear()
    curses.start_color()
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()

    blocks = get_pos(height // 2, width // 2)
    while True:
        paint_blocks(stdscr, blocks, "x")
        time.sleep(0.75)
        paint_blocks(stdscr, blocks, " ")
        blocks = cycle(blocks)


if __name__ == "__main__":
    curses.wrapper(main)
    exit(0)
