from typing import List   # , Tuple, Set, etc...


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


print(list_avg([5, 8, 9]))


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


class Animal:
    TYPES = ("Lion", "Monkey")

    def __init__(self, animal_type: str, gender: str, weight: int):
        self.animal_type = animal_type
        self.gender = gender
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Animal {self.animal_type}, {self.gender}, weighing {self.weight}g."

    # Note that we can't write -> Animal here, because it will give us an error. Because these lion and monkey method have created before the Animal class has finished proccessing. So these are creatd while the class is being processed. And we should put them inside qoutes. Also Note that if this returned a different class like Book, then we would write -> Book without putting inside qoutes.
    @classmethod
    def lion(cls, gender: str, weight: int) -> "Animal":
        return cls(cls.TYPES[0], gender, weight)

    @classmethod
    def monkey(cls, gender: str, weight: int) -> "Animal":
        return cls(cls.TYPES[1], gender, weight)


lion = Animal.lion("Male", 300)
print(lion)

monkey = Animal.monkey("Female", 45)
print(monkey)
