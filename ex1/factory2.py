from ex0.factory import CreatureFactory
from ex0.creature import Creature
from .heal import Sproutling, Bloomelle
from .transform import Shiftling, Morphagon


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
        return Shiftling("Shiflting", "\033[1;37m Normal\033[0m")

    def create_evolved(self) -> Creature:
        return Morphagon("Morphagon", "\033[1;37m Normal \033[0m/\033[1;31m"
                         "Dragon 🐉033[0m")

#Les classes concrètes suivantes héritent à la fois de Creature et de HealCapability :
# Sproutling et Bloomelle forment une seule famille et seront disponibles
# via HealingCreatureFactory (héritant de CreatureFactory).


# Les classes concrètes suivantes héritent à la fois de Creature et de TransformCapability : 
# Shiftling et Morphagon forment une seule famille et seront disponibles via 
# TransformCreatureFactory (héritant de CreatureFactory).