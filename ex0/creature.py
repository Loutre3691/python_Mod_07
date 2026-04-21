from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.type = creature_type

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower! ︻╦̵̵̿╤── 🔥🔥"


class Carapute(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!  ︻╦̵̵̿╤── 💦"


class Tortank(Creature):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump! 💧 "
