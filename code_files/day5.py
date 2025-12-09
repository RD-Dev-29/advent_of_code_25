from day_starter import DayStarter


class AdventDay5:

    def __init__(self):
        self.data = [x for x in DayStarter(5).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.fresh_ranges = []
        self.queries = []
        for line in self.data:
            if '-' in line:
                self.fresh_ranges.append([int(x) for x in line.split('-')])
            else:
                self.queries.append(int(line))
        self._merge_ranges()

    def process_queries(self):
        for query in self.queries:
            self.part1 += int(self._binary_search(query))

    def _binary_search(self, target):
        low, high = 0, len(self.fresh_ranges) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.fresh_ranges[mid][0] <= target and \
                    target <= self.fresh_ranges[mid][1]:
                return True
            elif target < self.fresh_ranges[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def count_total_fresh(self):
        total = 0
        for r in self.fresh_ranges:
            total += r[1] - r[0] + 1
        self.part2 = total

    def _merge_ranges(self):
        self.fresh_ranges.sort()
        merged = []
        for current in self.fresh_ranges:
            if not merged or merged[-1][1] < current[0] - 1:
                merged.append(current)
            else:
                merged[-1][1] = max(merged[-1][1], current[1])
        self.fresh_ranges = merged


if __name__ == '__main__':
    day5 = AdventDay5()
    day5.process_queries()
    day5.count_total_fresh()
    print(day5.part1, day5.part2)
