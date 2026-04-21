from ex0.creature import Creature
from abc import ABC, abstractmethod
from typing import Any


class TransformCapability(ABC):
    def __init__(self, result: bool) -> None:
        self.result = result

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self,  name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self, False)

    def transform(self) -> str:
        self.result = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.result = False
        return f"{self.name} returns to normal"

    def attack(self) -> str:
        if self.result is False:
            return f"{self.name} attacks normally"
        else:
            return f"{self.name} performs a boosted 🚀 strike!"


class Morphagon(Creature, TransformCapability):
    def __init__(self,  name: str, creature_type: str) -> None:
        Creature.__init__(self, name, creature_type)
        TransformCapability.__init__(self, False)


    def transform(self) -> str:
        self.result = True
        return f"{self.name} morphs into a dragonic battle form! 🗡️"

    def revert(self) -> str:
        self.result = False
        return f"{self.name} stabilizes its form"

    def attack(self) -> str:
        if self.result is False:
            return f"{self.name} attacks normally"
        else:
            return f"{self.name} unleashes a devastating morph strike!"
