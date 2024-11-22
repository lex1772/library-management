import pytest

from library_management import LibraryManagement


@pytest.fixture
def library(tmp_path):
    library_file = tmp_path / "test_library.json"
    library = LibraryManagement()
    library.file = str(library_file)
    return library


def test_load_no_file(library):
    library.file = ''
    library.load_library()
    assert library.library == []


def test_add_book(monkeypatch, library, capsys):
    inputs = iter([
        "Книга",
        "Автор",
        "неверный год",
        "2023"
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    library.add_book()

    captured = capsys.readouterr()
    assert "Год должен быть в числовом формате, введите число" in captured.out

    assert len(library.library) == 1
    assert library.library[0]["title"] == "Книга"
    assert library.library[0]["author"] == "Автор"
    assert library.library[0]["year"] == 2023


def test_delete_book_valid_id(monkeypatch, capsys):
    library = LibraryManagement()
    library.library = [
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1867, "status": "в наличии"},
        {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866, "status": "в наличии"},
    ]

    monkeypatch.setattr('builtins.input', lambda _: "1")
    library.delete_book()

    captured = capsys.readouterr()
    assert "Книга удалена" in captured.out
    assert len(library.library) == 1
    assert library.library[0]["id"] == 2


def test_delete_book_invalid_id(monkeypatch, capsys):
    library = LibraryManagement()
    library.library = [
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1867, "status": "в наличии"},
    ]

    monkeypatch.setattr('builtins.input', lambda _: "2")
    library.delete_book()

    captured = capsys.readouterr()
    assert "Книга с таким id не найдена" in captured.out
    assert len(library.library) == 1


def test_delete_book_non_integer_input(monkeypatch, capsys):
    library = LibraryManagement()
    library.library = [
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1867, "status": "в наличии"},
    ]

    inputs = iter(["некорректный id", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    library.delete_book()

    captured = capsys.readouterr()
    assert "Введите целое число" in captured.out
    assert "Книга удалена" in captured.out
    assert len(library.library) == 0


def test_search_book(monkeypatch, library, capsys):
    library.library = [
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1867, "status": "в наличии"},
        {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866, "status": "в наличии"},
        {"id": 3, "title": "Улитка на склоне", "author": "Братья Стругацкие", "year": 1972, "status": "в наличии"},
    ]
    library.save_library(library.library)

    monkeypatch.setattr('builtins.input', lambda _: "Война и мир")  # Ищем книгу по названию
    library.search_book()  # Поиск книги

    # Перехват вывода
    captured = capsys.readouterr()
    assert "Найденные книги:" in captured.out


def test_search_false_book(monkeypatch, library, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "Book" if _ == "Введите название книги: "
    else "Author" if _ == "Введите автора книги: "
    else "2024")
    library.add_book()

    monkeypatch.setattr('builtins.input', lambda _: "Magazine")
    library.search_book()

    captured = capsys.readouterr()
    assert "Книги не найдены" in captured.out


def test_show_all_books(library, capsys):
    library.library = [
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1867, "status": "в наличии"},
        {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866, "status": "в наличии"},
        {"id": 3, "title": "Улитка на склоне", "author": "Братья Стругацкие", "year": 1972, "status": "в наличии"},
    ]
    library.show_all_books()
    captured = capsys.readouterr()
    assert "Все книги:" in captured.out

    library.library = []
    library.show_all_books()
    captured = capsys.readouterr()
    assert "Библиотека пуста" in captured.out


def test_change_book_status(monkeypatch, library, capsys):
    library.library = [
        {"id": 1, "title": "Война и мир", "author": "Лев Толстой", "year": 1867, "status": "в наличии"},
        {"id": 2, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866, "status": "в наличии"},
        {"id": 3, "title": "Улитка на склоне", "author": "Братья Стругацкие", "year": 1972, "status": "в наличии"},
    ]

    inputs = iter(["1", "некорректный статус"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    library.change_status()

    captured = capsys.readouterr()
    assert "Некорректный статус" in captured.out

    inputs = iter(["1", "выдана"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    library.change_status()

    captured = capsys.readouterr()
    assert "Статус книги изменен" in captured.out

    inputs = iter(["5", "выдана"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    library.change_status()

    captured = capsys.readouterr()
    assert "Книга с таким id отсутствует" in captured.out
