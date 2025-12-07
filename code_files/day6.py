from day_starter import DayStarter
from math import prod


class AdventDay6:

    def __init__(self):
        self.data = DayStarter(6)
        self.part1 = 0
        self.part2 = 0

    def solve_part1(self):
        self.part1_data = [x.split() for x in self.data.splitlines()]
        for column in zip(*self.part1_data):
            if column[-1] == '*':
                self.part1 += prod(int(num) for num in column[:-1])
            elif column[-1] == '+':
                self.part1 += sum(int(num) for num in column[:-1])

    def solve_part2(self):
        self.part2_data = [x[::-1] for x in self.data.splitlines()]
        cur_vals = []
        for x in zip(*self.part2_data):
            try:
                cur_vals.append(int(''.join(x[:-1])))
            except ValueError:
                continue
            if x[-1] == '+':
                self.part2 += sum(cur_vals)
                cur_vals = []
            elif x[-1] == '*':
                self.part2 += prod(cur_vals)
                cur_vals = []


if __name__ == '__main__':
    day6 = AdventDay6()
    day6.solve_part1()
    day6.solve_part2()
    print(day6.part1, day6.part2)
