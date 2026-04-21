from ex1.factory1 import HealingCreatureFactory
from ex1.factory1 import TransformCreatureFactory as Trans
from ex1.heal import Sproutling, Bloomelle
from ex1.transform import Shiftling, Morphagon, TransformCapability


def test_healing_factory(heal_capability) -> None:
    print("\033[1;37m  base:\033[0m")
    base = heal_capability.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())

    evolved = heal_capability.create_evolved()
    print("\033[1;37m  evolved:\033[0m")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transforming_factory(transform_capability) -> None:
    print("\033[1;37m  base:\033[0m")
    base = transform_capability.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    base.transform()
    print(base.attack())
    print(base.revert())

    print("\033[1;37m  evolved:\033[0m")
    evolved = transform_capability.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    evolved.transform()
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    print("                               ,'\n\
    _.----.        ____         ,' _\\    ___    ___     ____\n\
_,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.\n\
\\     __     \\   '-.|    /   `.  ___    |    \\/    |   '-.   \\ |  |\n\
 \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |\n\
   \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n\
    \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     |\n\
     \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |\n\
      \\    \\ \\      /       `-.`.___,-' |  |\\  /| \\      /  | |   |\n\
       \\    \\ `.__,'|  |`-._    `|      |__| \\/ |  `.__,'|  | |   |\n\
        \\_.-'       |__|    `-._ |              '-.|     '-.| |   |\n\
                                `'                            '-._|")
    print("\n\033[1;37m === Testing Creature with healing "
          "capability === \033[0m\n")
    test_healing_factory(HealingCreatureFactory())

    print()

    print("\033[1;37m === Testing Creature with transform "
          "capability === \033[0m\n")
    test_transforming_factory(Trans())
