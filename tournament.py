from ex2.strategy import BattleStrategy, NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex0.factory import FlameFactory, AquaFactory
from ex1.factory1 import HealingCreatureFactory

def battle(tournament: list[tuple[objet, BattleFactory]]) -> None:
    print(tournament)
    print("\n\033[1;37m *** Tournament *** \033[0m\n")
    print(f"{len(tournament)} opponents involved")

    print("\n\033[1;37m* Battle *\033[0m\n")
    
        print(factory.create_base())
    


if __name__ == "__main__":
    print("\n\033[1;37m Tournament 0 (basic) \033[0m\n")
    tournament_0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingFactory(), DefensiveStrategy()),
    ]

    tournament_1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]

    tournament_2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformFactory(), AggressiveStrategy()),
    ]

    battle(tournament_0)
    battle(tournament_1)
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