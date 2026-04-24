from ex2.strategy import BattleStrategy, NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex0.factory import  FlameFactory, AquaFactory
from ex0.creature import Creature
from ex1.factory1 import HealingCreatureFactory, TransformCreatureFactory


def battle(tournament: list[tuple[Creature, BattleStrategy]]) -> None:
    dict_strat = {}

    for creature, strategy in tournament:
        dict_strat[creature] = strategy
        strategy.act()

    print("[ ", end="")
    for creature, strategy in dict_strat.items():
        print(f"({creature.name}+{strategy})", end=" ")
    print("]")

    print("\033[1;37m*** Tournament *** \033[0m")
    print(f"{len(tournament)} opponents involved")

    print("\n\033[1;37m* Battle *\033[0m")

    for i in range(len(tournament)):
        for j in range(i + 1, len(tournament)):
            creature = tournament[i]
            print(describe())
         
      


if __name__ == "__main__":
    print("\033[1;37mTournament 0 (basic) \033[0m")
    tournament_0 = [
        (FlameFactory().create_base(), NormalStrategy()),
        (HealingCreatureFactory().create_base(), DefensiveStrategy()),
    ]
    battle(tournament_0)

    print("\n\033[1;37mTournament 1 (error) \033[0m")
    tournament_1 = [
        (FlameFactory().create_base(), AggressiveStrategy()),
        (HealingCreatureFactory().create_base(), DefensiveStrategy()),
    ]
    battle(tournament_1)

    print("\n\033[1;37mTournament 2 (multiple) \033[0m")
    tournament_2 = [
        (AquaFactory().create_base(), NormalStrategy()),
        (HealingCreatureFactory().create_base(), DefensiveStrategy()),
        (TransformCreatureFactory().create_base(), AggressiveStrategy()),
    ]
    battle(tournament_2)

# 1 : creer plusieursfabrique de creature avec ex0 et ex1
# 2 : creer les 3 strategys (normal, defensiv et attaque)
# 3 : prendre une list d adversaire de tournois
#     chaque adversaire est un tupl e de fabrique de creature\
#     et d une strategie de combat
# 4: faire en sorte que chaque adversaire affronte tous les autres
#     une fois
# 5: organise les combats en utilisant la strategie associe a chaque 
#    creature
# 6: gerer les tuple de creature strategie invalide