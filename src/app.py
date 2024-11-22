from src.formatter import format_book
from src.commands import add_book_command, book_search_command, start_command, wrong_command, delete_command, book_issue_command
from src.config import book_repository

def start_app():
    command = start_command()
    match command.lower():
        case "добавить":
            new_book = add_book_command()
            book_repository.add_book(new_book)
            start_app()
        case "все":
            books = book_repository.get_all_books()
            if len(books) > 0:
                print("Сейчас в библиотеке лежат следующие книги:")
                for book in books:
                    format_book(book)
            else:
                print("Сейчас в библиотеке нет книг")
        case "удалить":
            book_id = delete_command()
            book_repository.delete_book(book_id)
        case "изменить":
            book_id = book_issue_command()
            book_repository.book_status_change(book_id)
        case "поиск":
            field, value = book_search_command()
            find_books = book_repository.search_book_by(field, value)
            if len(find_books) > 0:
                print("Найдены книги:")
                for book in find_books:
                    format_book(book)
            else:
                print("Ничего не найдено")
        case _:
            wrong_command()
    start_app()