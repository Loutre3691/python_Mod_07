from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def __str__(self) -> str:
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
    def __str__(self) -> str:
        return "Normal"

    def act(self) -> None:
        pass

    # def is_valid(self) -> bool:
    #     return True

# normal, adapte a toute creature, juste methode attack


class AggressiveStrategy(BattleStrategy):
    def __str__(self) -> str:
        return "Aggressive"

    def act(self) -> None:
        pass

    # def is_valid(self) -> bool:
    #     return True
# agressiv, creature transformable, se transforme attack et reprend leur forme initial


class DefensiveStrategy(BattleStrategy):
    def __str__(self) -> str:
        return "Defensive"

    def act(self) -> None:
        pass

    # def is_valid(self) -> bool:
    #     return True

# defensiv, creature qui se soigne, attque puis se soigne