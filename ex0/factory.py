from abc import ABC, abstractmethod
from .creature import Flameling, Pyrodon, Aquabub, Torragon, Creature


class CreatureFactory(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base(self) -> Creature:
        return Flameling("Flameling", "\033[1;31mFire 🔥\033[0m")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon", "🔥 \033[1;31mFire\033[0m/\033[1;37m"
                       "Flying 🪶\033[0m")


class AquaFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base(self) -> Creature:
        return Aquabub("Aquabub", "\033[1;36mWater 🌊\033[0m")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon", "\033[1;36mWater 🌊\033[0m")
