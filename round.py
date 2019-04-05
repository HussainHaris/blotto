class round:

    def __init__(self, armyOne, armyTwo):
        self.armyOne = armyOne
        self.armyTwo = armyTwo

    def evaluate(self):
        score_one = 0
        score_two = 0

        for castle in range(0, 10):
            castleValue = castle + 1

            if self.armyOne[castle] > self.armyTwo[castle]:
                score_one += castleValue
            elif self.armyOne[castle] < self.armyTwo[castle]:
                score_two += castleValue

            if score_one >= 20:
                winner = self.armyOne
                return winner, score_one
            elif score_two >= 20:
                winner = self.armyTwo
                return winner, score_two

            castleValue += 1

        if score_one >= score_two:
            winner = self.armyOne
            return winner, score_one
        elif score_two > score_one:
            winner = self.armyTwo
            return winner, score_two






