from abc import ABC, abstractmethod

class BattleStrategy(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def act(self) -> None:
        pass
# act sera appel dans le scrip du tournoi (action)
# si appele avec combinaison invalid, excetption avec message clair
    # @abstracmethod
    # def is_valid(self) -> bool:
    #     return True
# renvoie true si la creature est compatible avec
# la strategie et false le contraire


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        pass

    def act(self) -> None:
        pass

    # def is_valid(self) -> bool:
    #     return True

# normal, adapte a toute creature, juste methode attack

class AggressiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        pass

    def act(self) -> None:
        pass

    # def is_valid(self) -> bool:
    #     return True
# agressiv, creature transformable, se transforme attack et reprend leur forme initial

class DefensiveStrategy(BattleStrategy):
    def __init__(self) -> None:
        pass

    def act(self) -> None:
        pass

    # def is_valid(self) -> bool:
    #     return True

# defensiv, creature qui se soigne, attque puis se soigne