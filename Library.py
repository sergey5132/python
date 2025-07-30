# Библиотека.

# Создайте класс Library, который будет представлять библиотеку книг.
# Добавьте метод __str__, который будет возвращать строку с информацией о библиотеке с перечнем книг, и метод __len__,
# который будет возвращать количество книг в библиотеке.
# Создайте объект класса Library, добавьте в него несколько книг и
# выведите информацию о библиотеке с перечнем книг и количество книг.

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
# Напишите тут ваш код
        self.books.append(book)

    def __str__(self):
        return f'{self.books}'

    def __len__(self):
        return len(self.books)



# Создаем объект библиотеки
library = Library()

# Добавляем книги в библиотеку
library.add_book("Harry Potter and the Philosopher's Stone")
library.add_book("The Great Gatsby")
library.add_book("1984")

# Выводим информацию о библиотеке с перечнем книг и количество книг
print(library)
print(f"Number of books in library: {len(library)}")

