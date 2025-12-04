from day_starter import DayStarter

adjacant_directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, -1), (1, 1)]


class AdventDay4:

    def __init__(self):
        self.data = [x for x in DayStarter(4).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0
        self.removal_stack = []

    def _process_data(self):
        self.ROWS = len(self.data)
        self.COLS = len(self.data[0])
        self.data = [list(row) for row in self.data]

    def part_one(self):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.data[i][j] == '@':
                    if self._search_adjacent(i, j):
                        self.part1 += 1

    def part_two(self):
        while self.removal_stack:
            for _ in range(len(self.removal_stack)):
                i, j = self.removal_stack.pop()
                self.part2 += 1
                self.data[i][j] = '.'
            for i in range(self.ROWS):
                for j in range(self.COLS):
                    if self.data[i][j] == '@':
                        self._search_adjacent(i, j)

    def _search_adjacent(self, i, j):
        roll_count = 0
        for di, dj in adjacant_directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < self.ROWS and 0 <= nj < self.COLS
                    and self.data[ni][nj] == '@'):
                roll_count += 1
        if roll_count < 4:
            self.removal_stack.append((i, j))
        return roll_count < 4


if __name__ == '__main__':
    day4 = AdventDay4()
    print(day4.data)
    day4.part_one()
    day4.part_two()
    print(day4.part1, day4.part2)
