from day_starter import DayStarter


class AdventDay3:

    def __init__(self):
        self.data = [x for x in DayStarter(3).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        pass

    def part_one(self):
        for line in self.data:
            self.part1 += self._find_best(line, 2)

    def part_two(self):
        for line in self.data:
            self.part2 += self._find_best(line, 12)

    def _find_best(self, line, target_length):
        cur_best = ['0'] * target_length
        n = len(line)
        for i in range(n):
            for j in range(target_length):
                # for each position in the target, see if we can improve it.
                # we can only improve it if there are enough characters left
                # in the full line to fill the remaining positions.
                # If so, update the current best and reset all subsequent
                # positions to '0' to allow for future filling.
                if line[i] > cur_best[j] and n - i >= target_length - j:
                    cur_best[j] = line[i]
                    for k in range(j + 1, target_length):
                        cur_best[k] = '0'
                    break
        return int(''.join(cur_best))


if __name__ == '__main__':
    day3 = AdventDay3()
    day3.part_one()
    day3.part_two()
    print(day3.part1, day3.part2)
