from day_starter import DayStarter


class AdventDay2:

    def __init__(self):
        self.data = [x for x in DayStarter(2).split(',')]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.vals_to_check = []
        for r1, r2 in [tuple(map(int, x.split('-'))) for x in self.data]:
            self.vals_to_check.extend(list(range(r1, r2 + 1)))
            self.vals_to_check = list(set(self.vals_to_check))

    def solve(self):
        for num in self.vals_to_check:
            str_num = str(num)
            n = len(str_num)

            # Check for part 1 and 2: repeats twice only
            if n % 2 == 0:
                mid = n // 2
                left, right = str_num[:mid], str_num[mid:]
                if left == right:
                    self.part1 += num
                    self.part2 += num
                    continue

            # Check for part 2: repeats any amount of times
            if n < 2:
                continue
            str_factors = self._factor(n)
            for f in str_factors:
                init_part = str_num[:f]
                if all(init_part == str_num[j:j+f] for j in range(f, n, f)):
                    self.part2 += num
                    break

    def _factor(self, n):
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i and i > 1:
                    factors.append(n // i)
        return factors


if __name__ == '__main__':
    day2 = AdventDay2()
    day2.solve()
    print(day2.part1, day2.part2)
