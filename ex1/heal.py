from abc import ABC, abstractmethod
from ex0.creature import Sproutling, Bloomelle


class HealCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def heal(self) -> str:
        pass


class Sproutling(HealCapability):
    def __init__(self) -> None:
        pass

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(HealCapability):
    def __init__(self) -> None:
        pass

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"
    
