import doctest

class Spacecraft:
    def __init__(self, model: str, speed: float):
        """
        Инициализирует объект Космический корабль
        model: Модель космического корабля
        speed: Скорость космического корабля
        """
        self.model = model
        self.speed = speed
        self.position = (0, 0, 0)  # (x, y, z) координаты в пространстве

    def move_to(self, destination: tuple) -> None:
        """
        Перемещает космический корабль в указанное место.
        Координаты (x, y, z) места, куда переместить корабль
        """
        self.position = destination
        print(f"{self.model} is moving to position {destination}.")

    def explore(self) -> None:
        """ 
        Запускает исследование космоса
        """
        print(f"{self.model} is exploring the cosmos.")

class Astronaut:
    def __init__(self, name: str, age: int, space_experience: int):
        """
        Инициализирует объект Астронавт

        name: Имя астронавта
        age: Возраст астронавта
        space_experience: Опыт полетов в космосе
        """
        self.name = name
        self.age = age
        self.space_experience = space_experience

    def conduct_experiment(self) -> None:
        """
        Проводит научный эксперимент в космосе.
        """
        print(f"Astronaut {self.name} is conducting a space experiment.")

    def spacewalk(self) -> None:
        """
        Осуществляет выход в открытый космос.
        """
        print(f"Astronaut {self.name} is performing a spacewalk.")

class Planet:
    def __init__(self, name: str, research_type: str, has_atmosphere: bool):
        """
        Инициализирует объект Планета

        name: Название планеты
        research_type: Тип исследования
        has_atmosphere: Наличие атмосферы на планете
        """
        self.name = name
        self.research_type = research_type
        self.has_atmosphere = has_atmosphere

    def analyze_atmosphere(self) -> None:
        """
        Анализирует атмосферу планеты.
        """
        if self.has_atmosphere:
            print(f"Researchers are analyzing the atmosphere of exoplanet {self.name}.")
        else:
            print(f"Planet {self.name} does not have an atmosphere.")

if __name__ == "__main__":
    doctest.testmod()
