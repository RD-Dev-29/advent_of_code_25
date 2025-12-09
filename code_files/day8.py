from day_starter import DayStarter
from math import prod


class AdventDay8:

    def __init__(self):
        self.data = [x for x in DayStarter(8).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.data = [tuple(map(int, x.split(','))) for x in self.data]
        self.connection_scores = []
        n = len(self.data)
        for i in range(n - 1):
            for j in range(i + 1, n):
                self.connection_scores.append(
                    [self._distance(self.data[i], self.data[j]), (i, j)])
        self.connection_scores.sort(key=lambda x: x[0])
        self.connection_scores = self.connection_scores

    def group_connections(self):
        groups: list[set] = []
        for score, indices in self.connection_scores[:1000]:
            found_group = False
            for group in groups:
                if indices[0] in group or indices[1] in group:
                    group.update(set(indices))
                    found_group = True
                    break
            if not found_group:
                groups.append(set(indices))

        found_connection = True
        while found_connection:
            found_connection = False
            for i in range(len(groups) - 1):
                for j in range(i + 1, len(groups)):
                    if groups[i].intersection(groups[j]):
                        groups[i].update(groups[j])
                        del groups[j]
                        found_connection = True
                        break
                if found_connection:
                    break

        print(groups)
        self.part1 = prod(sorted([len(g) for g in groups])[-3:])

    def solve_part2(self):
        seen = set()
        for score, indices in self.connection_scores:
            seen.update(indices)
            if len(seen) == len(self.data):
                self.part2 = (self.data[indices[1]][0] *
                              self.data[indices[0]][0])
                break

    def _distance(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


if __name__ == '__main__':
    day8 = AdventDay8()
    day8.group_connections()
    day8.solve_part2()
    print(day8.part1, day8.part2)
