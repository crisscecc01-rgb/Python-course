class Move:
    def __init__(self, name, move_type, category, power, accuracy, pp, effect):
        self.name = name
        self.type = move_type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.effect = effect

    def move_copy(self):
        return Move(
            self.name,
            self.type,
            self.category,
            self.power,
            self.accuracy,
            self.pp,
            effect=self.effect.copy() if self.effect else None
        )
