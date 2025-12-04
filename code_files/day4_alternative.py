from day_starter import DayStarter
from collections import defaultdict

adjacant_directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, -1), (1, 1)]


class AdventDay4:

    def __init__(self):
        self.data = [list(x)for x in DayStarter(4).split()]
        self.roll_dict = defaultdict(int)
        self.process_data()
        self.part1 = 0
        self.part2 = 0

    def process_data(self):
        self.N = len(self.data)
        for i in range(self.N):
            for j in range(self.N):
                if self.data[i][j] == '@':
                    self.roll_dict[(i, j)] = self._search_adjacent(i, j)

    def part_one(self):
        self.part1 = sum(1 for count in self.roll_dict.values() if count < 4)

    def part_two(self):
        self.removal_stack = set([pos for pos, count in
                                  self.roll_dict.items() if count < 4])
        while self.removal_stack:
            self.part2 += 1
            i, j = self.removal_stack.pop()
            self.roll_dict.pop((i, j), None)
            self._search_adjacent(i, j, False)

    def _search_adjacent(self, i, j, initial=True):
        roll_count = 0
        for di, dj in adjacant_directions:
            ni, nj = i + di, j + dj
            if initial:
                if (0 <= ni < self.N and 0 <= nj < self.N
                        and self.data[ni][nj] == '@'):
                    roll_count += 1
            else:
                if (ni, nj) in self.roll_dict:
                    self.roll_dict[(ni, nj)] -= 1
                    if self.roll_dict[(ni, nj)] < 4:
                        self.removal_stack.add((ni, nj))
        return roll_count


if __name__ == '__main__':
    day4 = AdventDay4()
    day4.part_one()
    day4.part_two()
    print(day4.part1, day4.part2)
