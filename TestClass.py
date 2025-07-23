class TestClass:

    attribut = "I work in Russia"
    def instance_metod(self):
        print(type(self))
        print(self.attribut)

    def set_attribut(self, name):
        self.attribut = name
    def print_attribut(self):
        print(self.attribut)

    @classmethod
    def class_metod(cls):
        print(type(cls))
        print(cls.attribut)
        print(TestClass.attribut)

    @staticmethod
    def static_metod():
        print('static metod')




myobj = TestClass()
myobj.attribut = "i work in Belarus"

myobj.instance_metod()
TestClass.class_metod()

TestClass.static_metod()

myobj.static_metod()


# Создаем классы.

# Создайте класс Library с атрибутом books, который представляет собой список книг.
# Добавьте методы add_book(book) для добавления книги в библиотеку
# и display_books() для вывода списка всех книг.
# Создайте объект класса Library, добавьте несколько книг и выведите список книг, используя методы объекта.

# Напишите тут ваш код

class Library:
    def __init__(self):
        self.books = []

    def display_books(self):
        for book in self.books:
            print(book)

    def add_book(self, book):
        self.books.append(book)


lib = Library()

lib.add_book("wecwec")
lib.add_book("wecwecwwecwec")

lib.display_books()