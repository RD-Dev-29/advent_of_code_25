from day_starter import DayStarter


class AdventDay1:

    def __init__(self):
        self.data = [x for x in DayStarter(1).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0
        self.position = 50

    def _process_data(self):
        pass

    def complete_turns(self):
        for item in self.data:
            direction = item[0]
            steps = int(item[1:])
            self._turn_dial(direction, steps)
            if self.position == 0:
                self.part1 += 1

    def _turn_dial(self, direction, steps):
        temp = steps
        while temp > 0:
            if direction == 'R':
                self.position += 1
            elif direction == 'L':
                self.position -= 1
            temp -= 1
            if self.position > 99:
                self.position -= 100
            elif self.position < 0:
                self.position += 100
            if self.position == 0:
                self.part2 += 1


if __name__ == '__main__':
    day1 = AdventDay1()
    day1.complete_turns()
    print(day1.part1, day1.part2)
