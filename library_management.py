import json
from typing import List, Dict, Any


class LibraryManagement:
    def __init__(self) -> None:
        self.file: str = 'library.json'
        self.library: List[Dict[str, Any]] = self.load_library()
        self.last_id: int = self.find_last_id()

    def find_last_id(self) -> int:
        """Метод для нахождения последнего id в файле.

        Returns:
            int: Последний идентификатор книги. Если библиотека пуста, возвращает 0.
        """
        if self.library:
            return int(self.library[-1]['id'])
        else:
            return 0

    def load_library(self) -> List[Dict[str, Any]]:
        """Метод загружает список словарей с данными о книгах.

        Returns:
            List[Dict[str, Any]]: Список словарей, где каждый словарь содержит данные о книге.
            Если файл не найден, возвращает пустой список.
        """
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_library(self, library) -> None:
        """Метод сохраняет словарь с данными книги в файл"""
        with open(self.file, "w") as f:
            json.dump(library, f)

    def add_book(self) -> None:
        """Метод для добавления данных книги в файл"""
        title: str = str(input("Введите название книги: "))
        author: str = str(input("Введите автора книги: "))
        book_id: int = self.last_id + 1
        self.last_id += 1

        while True:
            try:
                year: int = int(input("Введите год издания: "))
                break
            except ValueError:
                print("Год должен быть в числовом формате, введите число")

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии",
        }

        self.library.append(book)
        self.save_library(self.library)
        print(f"Книга {title} c id {book_id} добавлена")

    def delete_book(self) -> None:
        """Метод для удаления книгу из файла."""
        while True:
            try:
                book_id: int = int(input("Введите id книги которую требуется удалить: "))
                break
            except ValueError:
                print("Введите целое число")
        for i, book in enumerate(self.library):
            if int(book["id"]) == book_id:
                del self.library[i]
                self.save_library(self.library)
                print("Книга удалена")
                return
        print("Книга с таким id не найдена")

    def search_book(self) -> None:
        """Метод для поиска книги по названию, автору или году"""
        search_word: str = input("Введите название, автора или год издания для поиска книг: ")
        results: List[Dict[str, Any]] = []
        for book in self.library:
            if search_word.lower() == book["title"].lower() or \
                    search_word.lower() == book["author"].lower() or \
                    search_word == str(book["year"]):
                results.append(book)
        if results:
            print("Найденные книги:")
            for book in results:
                print(book)
        else:
            print("Книги не найдены")

    def show_all_books(self) -> None:
        """Метод для вывода всех книг"""
        if self.library:
            print("Все книги:")
            for book in self.library:
                print(book)
        else:
            print("Библиотека пуста")

    def change_status(self) -> None:
        """Метод для изменения статус книги"""
        book_id: int = int(input("Введите id книги для изменения статуса: "))
        new_status: str = input("Введите новый статус (возможен статус только'в наличии' или 'выдана'): ")
        for book in self.library:
            if int(book["id"]) == book_id:
                if new_status.lower() in ["в наличии", "выдана"]:
                    book["status"] = new_status
                    self.save_library(self.library)
                    print("Статус книги изменен")
                    return
                else:
                    print("Некорректный статус")
                    return
        print("Книга с таким id отсутствует")


def main() -> None:
    """Основная функция"""
    library = LibraryManagement()
    while True:
        print("Меню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        user_choice: str = input("Выберите пункт меню: ")

        if user_choice == "1":
            library.add_book()
        elif user_choice == "2":
            library.delete_book()
        elif user_choice == "3":
            library.search_book()
        elif user_choice == "4":
            library.show_all_books()
        elif user_choice == "5":
            library.change_status()
        elif user_choice == "6":
            break
        else:
            print("Такого варианта нет")


if __name__ == "__main__":
    main()
