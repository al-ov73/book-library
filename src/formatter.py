from src.models import Book


def format_book(book: Book) -> str:
    print(f"id:{book.id}, название: \"{book.title}\", автор: \"{book.author}\", год издания: {book.year}, статус: \"{book.status}\"")