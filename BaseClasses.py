import Database as Db

class HealClass:
    def __init__(self, name, number):
        self.name = name
        self.effect = Db.I_db.heals_dict[name]
        self.number = number

    def __str__(self):
        return f"{self.number} x {self.name} (--> +{self.effect})"
    def __repr__(self):
        return str(self)

class PokeBallClass:
    def __init__(self, name, number):
        self.name = name
        self.catch_rate = Db.I_db.pokeball_dict[name]
        self.number = number

    def __str__(self):
        return f"{self.number} x {self.name} (--> {self.catch_rate})"

    def __repr__(self):
        return str(self)

class Move:
    def __init__(self, name, move_type, category, power, accuracy, pp, effect):
        self.name = name
        self.type = move_type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.effect = effect

def move_copy(row):
    return Move(
        name=row["name"],
        move_type=row["type"],
        category=row["category"],
        power=row["power"],
        accuracy=row["accuracy"],
        pp=row["pp"],
        effect=None
    )






