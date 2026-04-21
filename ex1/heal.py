from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def heal(self) -> str:
        pass


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip 🍇!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__(name, creature_type)

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance 💃🌸!"

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"
