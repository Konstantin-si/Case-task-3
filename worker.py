from dataclasses import dataclass
from datetime import datetime


@dataclass
class Worker:
    full_name: str
    position: str
    salary: float
    start_year: int

    def __init__(self, full_name: str = "Не указано",
                 position: str = "Не указано",
                 salary: float = 0.0,
                 start_year: int = 0):
        self.full_name = full_name
        self.position = position
        self.salary = salary if salary > 0 else 0.0
        self.start_year = start_year

    @classmethod
    def from_name_position(cls, full_name: str, position: str):
        return cls(full_name, position, 0.0, datetime.now().year)

    def get_experience(self, current_year: int = None) -> int:
        if current_year is None:
            current_year = datetime.now().year
        return current_year - self.start_year

    def __str__(self) -> str:
        return (f"ФИО: {self.full_name}, Должность: {self.position}, "
                f"Зарплата: {self.salary:.2f} руб., Год поступления: {self.start_year}")

    def __del__(self):
        print(f"Объект Worker {self.full_name} уничтожен.")
