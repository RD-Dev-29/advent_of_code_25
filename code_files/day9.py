from day_starter import DayStarter


class AdventDay9:

    def __init__(self):
        self.data = [x for x in DayStarter(9).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.data = [tuple(map(int, x.split(','))) for x in self.data]

    def largest_rectangle(self):
        n = len(self.data)
        self.areas = []
        for i in range(n):
            for j in range(i + 1, n):
                width = abs(self.data[j][0] - self.data[i][0]) + 1
                height = abs(self.data[j][1] - self.data[i][1]) + 1
                area = width * height
                self.areas.append([area, (i, j)])
        self.areas.sort(reverse=True)
        self.part1 = self.areas[0][0]

    def _shape_perimeter(self):
        self.perimeter = set()
        for i in range(len(self.data)):
            x1, y1 = self.data[i - 1]
            x2, y2 = self.data[i]
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    self.perimeter.add((x1, y))
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    self.perimeter.add((x, y1))

    def largest_inner_rectangle(self):
        self._shape_perimeter()
        for area, (i, j) in self.areas:
            x_min = min(self.data[i][0], self.data[j][0])
            x_max = max(self.data[i][0], self.data[j][0])
            y_min = min(self.data[i][1], self.data[j][1])
            y_max = max(self.data[i][1], self.data[j][1])
            bad = False
            for x, y in self.perimeter:
                if x_min < x < x_max and y_min < y < y_max:
                    bad = True
                    break
            if bad:
                continue
            self.part2 = area
            break


if __name__ == '__main__':
    day9 = AdventDay9()
    day9.largest_rectangle()
    day9.largest_inner_rectangle()
    print(day9.part1, day9.part2)
