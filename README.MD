## Консольное приложение для управления библиотекой книг

Приложение позволяет добавлять, удалять, искать и отображать книги. Каждая книга содержит следующие поля:

 • id (уникальный идентификатор, генерируется автоматически)

 • title (название книги)

 • author (автор книги)

 • year (год издания)

 • status (статус книги: “в наличии”, “выдана”)

Покрытие тестами осуществлено на 77%



## Как пользоваться?

В начале необходимо установить зависимости командой:

    pip install -r requirements.txt

Затем пользователь запускает скрипт, после чего приложение предлагает выбрать 6 пунктов на выбор для ввода целого числа в консоль:

 1. Добавление книги: Пользователь вводит title, author и year в формате int, после чего книга добавляется в файл с уникальным id и статусом “в наличии”.

 2. Удаление книги: Пользователь вводит id книги в формате int, которую нужно удалить. Если книга существует, то она удаляется, если же такой книги нет, то пользователю приходит сообщение "Книга с таким id не найдена"

 3. Поиск книги: Пользователь может искать книги по title, author или year. Если такая книга есть, то вернется словарь с ее данными. В ином случае ответ будет "Книги не найдены"

 4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status. Если же список книг пустой, то приложение возвращает "Библиотека пуста"

 5. Изменение статуса книги: Пользователь вводит id книги в формате int и новый статус (“в наличии” или “выдана”). Если выбран иной статус, то приложение выведет сообщение "Некорректный статус". Если id книги отсутствует в библиотеке, то приложеные выведет "Книга с таким id отсутствует"

 6. Выход из приложения.

В ином случае приложение выведет "Такого варианта нет"

## Стек технологий:

    Python 3
    Pytest (для тестов)
    Coverage (для тестов)