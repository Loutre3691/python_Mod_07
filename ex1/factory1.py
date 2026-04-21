from ex0.factory import CreatureFactory
from ex0.creature import Creature
from ex1.transform import Shiftling, Morphagon
from ex1.heal import Sproutling, Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base(self) -> Creature:
        return Sproutling("Sproutling", "\033[1;32mGrass 🌱 \033[0m")

    def create_evolved(self) -> Creature:
        return Bloomelle("Bloomelle", "\033[1;32m🌱 Grass\033[0m/\033[1;35m"
                         "Fairy 🧚\033[0m")


class TransformCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        pass

    def create_base(self) -> Creature:
        return Shiftling("Shiftling", "\033[1;37mNormal\033[0m")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "\033[1;37mNormal\033[0m/"
                         "\033[1;31mDragon 🐉\033[0m")
 