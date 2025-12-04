from day_starter import DayStarter

adjacant_directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, -1), (1, 1)]


class AdventDay4:

    def __init__(self):
        self.data = [list(x)for x in DayStarter(4).split()]
        self.N = len(self.data)
        self.part1 = 0
        self.part2 = 0
        self.removal_stack = []

    def part_one(self):
        self._search_map()
        self.part1 = len(self.removal_stack)

    def part_two(self):
        while self.removal_stack:
            for _ in range(len(self.removal_stack)):
                i, j = self.removal_stack.pop()
                self.part2 += 1
                self.data[i][j] = '.'
            self._search_map()

    def _search_map(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.data[i][j] == '@':
                    self._search_adjacent(i, j)

    def _search_adjacent(self, i, j):
        roll_count = 0
        for di, dj in adjacant_directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < self.N and 0 <= nj < self.N
                    and self.data[ni][nj] == '@'):
                roll_count += 1
        if roll_count < 4:
            self.removal_stack.append((i, j))


if __name__ == '__main__':
    day4 = AdventDay4()
    day4.part_one()
    day4.part_two()
    print(day4.part1, day4.part2)
