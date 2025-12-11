from day_starter import DayStarter
from functools import cache


class AdventDay11:

    def __init__(self):
        self.data = [x for x in DayStarter(11).split('\n')]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.mapping = {}
        for line in self.data:
            if line == '':
                continue
            key, values = line.split(': ')
            self.mapping[key] = values.split(' ')

    def part_one_solution(self):
        self.part1 += self._traverse_mapping('you')

    def part_two_solution(self):
        self.part2 += self._traverse_mapping('svr', constraint=('dac', 'fft'))

    @cache
    def _traverse_mapping(self, current, constraint=()):
        if current == 'out':
            return len(constraint) == 0
        if current in constraint:
            constraint = tuple(x for x in constraint if x != current)
        return sum([self._traverse_mapping(neighbor, constraint)
                    for neighbor in self.mapping[current]])


if __name__ == '__main__':
    day11 = AdventDay11()
    day11.part_one_solution()
    day11.part_two_solution()
    print(day11.part1, day11.part2)
