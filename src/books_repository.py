import json
from src.models import Book


class BookRepository:
    STORAGE_PATH = 'src/library.json'

    @staticmethod
    def _dict_to_book(input_book: dict) -> Book | None:
        try:
            return Book(
                id=input_book["id"],
                title=input_book["title"],
                author=input_book["author"],
                year=input_book["year"],
                status=input_book["status"]
            )
        except KeyError:
            return None

    @staticmethod
    def _book_to_dict(input_book: Book) -> dict:
        print(input_book.status)
        return {
            "id": input_book.id,
            "title": input_book.title,
            "author": input_book.author,
            "year": input_book.year,
            "status": input_book,
        }

    def get_all_books(self) -> list[Book]:
        try:
            with open(self.STORAGE_PATH, "r", encoding="utf-8") as f:
                books_list = json.load(f)
                converted_books = map(self._dict_to_book, books_list)
                return list(filter(None, converted_books))
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            return []

    def add_book(self, book: Book):
        library = self.get_all_books()
        library.append(book)
        updated_lib_dict = list(map(self._book_to_dict, library))
        with open(self.STORAGE_PATH, "w", encoding="utf-8") as file:
            json.dump(updated_lib_dict, file)
        print(f"Добавлена книга с id: {book.id}")
            
    def get_next_id(self) -> int:
        library = self.get_all_books()
        try:
            print(library)
            last_book = library[-1]
            return last_book.id + 1
        except IndexError:
            return 1
        
    def delete_book(self, input_id: int) -> None:
        library = self.get_all_books()
        updated_lib = filter(lambda book: book.id != input_id, library)
        updated_lib_dict = list(map(self._book_to_dict, updated_lib))
        with open(self.STORAGE_PATH, "w", encoding="utf-8") as file:
            json.dump(updated_lib_dict, file)
        print(f"Удалена книга с id: {input_id}")

    def book_status_change(self, input_id: int) -> None:
        library = self.get_all_books()
        book = [book for book in library if book.id == input_id][0]
        # IndexError:
        index = library.index(book)
        before = book.status
        book.status = "В наличии" if book.status == "Выдана" else "Выдана"
        print(f"Статус книги с id: {book.id} изменен с {before} на {book.status}")
        library[index] = book
        updated_lib_dict = list(map(self._book_to_dict, library))
        with open(self.STORAGE_PATH, "w", encoding="utf-8") as file:
            json.dump(updated_lib_dict, file)