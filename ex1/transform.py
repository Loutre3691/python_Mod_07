from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(TransformCapability):
    def __init__(self) -> None:
        super().__init__()

    def transform(self) -> str:
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        return "Shiftling returns to normal"


class Morphagon(TransformCapability):
    def __init__(self) -> None:
        super().__init__()

    def transform(self) -> str:
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        return "Morphagon stabilizes its form"
