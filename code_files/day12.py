from day_starter import DayStarter


class AdventDay12:

    def __init__(self):
        self.data = [x for x in DayStarter(12).split('\n')]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.piece_parts = self.data[:30]
        self.plans = self.data[30:-1]
        self.pieces = {}
        for i in range(6):
            piece = []
            for j in range(1, 4):
                piece.append(self.piece_parts[i * 5 + j])
            self.pieces[i] = {'piece': piece,
                              'count': sum(row.count('#')
                                           for row in piece)}

    def solve_part1(self):
        for plan in self.plans:
            size, presents = plan.split(': ')
            area = int(size.split('x')[0]) * int(size.split('x')[1])
            presents = [int(x) for x in presents.split(' ')]
            used = 0
            for i, present in enumerate(presents):
                used += self.pieces[i]['count'] * present
            if used <= area:
                self.part1 += 1


if __name__ == '__main__':
    day12 = AdventDay12()
    day12.solve_part1()
    print(day12.part1, day12.part2)
