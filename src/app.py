from src.commands import add_book_command, start_command, wrong_command, delete_command, book_issue_command
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
            print("Сейчас в библиотеке лежат следующие книги:")
            for index, book in enumerate(books):
                print(f"id:{book.id}, название: {book.title}, автор: {book.author}, год издания: {book.year}, статус: {book.status}")
        case "удалить":
            book_id = delete_command()
            book_repository.delete_book(book_id)
        case "изменить":
            book_id = book_issue_command()
            book_repository.book_status_change(book_id)
        case _:
            wrong_command()
    start_app()