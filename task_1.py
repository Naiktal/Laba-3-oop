class Book:
    "Базовый класс книги."
    def __init__(self, name: str, author: str):
        self._name = name #protected атрибут
        self._author = author #protected атрибут

    # для того, чтобы атрибуты не могли изменяться
    @property
    def name(self) -> str:
        return self._name
    @property
    def author(self) -> str:
        return self._author

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @author.setter
    def author(self, author: str) -> None:
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter #накладывание ограничений на атрибут
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    # перегрузка метода, так как родительский класс не предполагает вывода количества страниц
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter #накладывание ограничений на атрибут
    def duration(self, duration: int) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть числом с плавающей запятой")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
        self._duration = duration

    # перегрузка метода, так как родительский класс не предполагает вывода продолжительности
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"

#Проверка классов

if __name__ == '__main__':
    na = AudioBook("HarryP", "JKRow", 556.22)
    nw = PaperBook("Mas_and_Marg", "Bulgakov", 442)
    list = [na, nw]
    print(na)
    print(nw)
    print(list)
