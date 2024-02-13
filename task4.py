from abc import ABC, abstractmethod

class SpaceBody(ABC):

    def __init__(self, name: str, mass: float, radius: float, color: str = "серый"):

        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color

    @abstractmethod
    def gravity(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.name} ({self.__class__.__name__})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.mass}, {self.radius}, color='{self.color}')"


class Planet(SpaceBody):

    def __init__(self, name: str, mass: float, radius: float, color: str = "синий", has_atmosphere: bool = True):
        super().__init__(name, mass, radius, color)
        self.has_atmosphere = has_atmosphere

    def gravity(self) -> float:
        return 6.67430e-11 * self.mass / (self.radius * 1000) ** 2

    def __str__(self) -> str:
        return f"{super().__str__()}, цвет: {self.color}, атмосфера: {'да' if self.has_atmosphere else 'нет'}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.mass}, {self.radius}, color='{self.color}', has_atmosphere={self.has_atmosphere})"


class Space(SpaceBody):

    def gravity(self) -> float:
        return 0

    def __str__(self) -> str:
        return f"{self.__class__.__name__}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
