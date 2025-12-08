from day_starter import DayStarter
from collections import defaultdict


class AdventDay7:

    def __init__(self):
        self.data = [x for x in DayStarter(7).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.beams = {self.data[0].index('S'): 1}

    def solve(self):
        for i in range(1, len(self.data)):
            line = self.data[i]
            new_beams = defaultdict(int)
            for k, v in self.beams.items():
                if line[k] == '.':
                    new_beams[k] += v
                else:
                    # any split increases part 1 count
                    self.part1 += 1
                    new_beams[k - 1] += v
                    new_beams[k + 1] += v
            self.beams = new_beams
        # final count of beam values is part 2
        self.part2 = sum(self.beams.values())


if __name__ == '__main__':
    day7 = AdventDay7()
    day7.solve()
    print(day7.part1, day7.part2)
