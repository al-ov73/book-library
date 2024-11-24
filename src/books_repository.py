import json

from src.models import Book


class BookRepository:
    STORAGE_PATH = 'src/library.json'

    @staticmethod
    def _lib_to_books(library: list[dict]) -> list[Book]:
        """
        convert list of dicts from .json file to list of Book objects
        """
        books_lib = []
        for book in library:
            try:
                books_lib.append(
                    Book(
                        id=book["id"],
                        title=book["title"],
                        author=book["author"],
                        year=book["year"],
                        status=book["status"]
                    )
                )
            except KeyError:
                continue
        return books_lib

    @staticmethod
    def _lib_to_dict(library: list[Book]) -> list[dict]:
        """
        convert list of Book objects to list of dicts to load it to .json file
        """
        dict_lib = []
        for book in library:
            dict_lib.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "year": book.year,
                    "status": book.status,
                }
            )
        return dict_lib

    def get_all_books(self) -> list[Book]:
        """
        return list of Book objects from .json library file
        """
        try:
            with open(self.STORAGE_PATH, "r", encoding="utf-8") as f:
                books_list = json.load(f)
                return self._lib_to_books(books_list)
        except FileNotFoundError:
            return []
        except json.decoder.JSONDecodeError:
            return []

    def add_book(self, book: Book):
        """
        get Book and add it to library .json file
        """
        library = self.get_all_books()
        library.append(book)
        updated_lib_dict = self._lib_to_dict(library)
        with open(self.STORAGE_PATH, "w", encoding="utf-8") as file:
            json.dump(updated_lib_dict, file, ensure_ascii=False)
        print(f"Добавлена книга с id: {book.id}")

    def get_next_id(self) -> int:
        """
        return id = las_book_id + 1 to use it for next book
        """
        library = self.get_all_books()
        try:
            last_book = library[-1]
            return last_book.id + 1
        except IndexError:
            return 1

    def delete_book(self, input_id: int) -> None:
        """
        get id: int and delete book with such id
        """
        library = self.get_all_books()
        updated_lib = list(filter(lambda book: book.id != input_id, library))
        if len(library) == len(list(updated_lib)):
            print("Такой книги не существует!")
        else:
            updated_lib_dict = self._lib_to_dict(updated_lib)
            with open(self.STORAGE_PATH, "w", encoding="utf-8") as file:
                json.dump(updated_lib_dict, file, ensure_ascii=False)
            print(f"Удалена книга с id: {input_id}")

    def book_status_change(self, input_id: int) -> None:
        """
        get id: int and change status of book 'В наличии' <-> 'Выдана'
        """
        library = self.get_all_books()
        try:
            book = [book for book in library if book.id == input_id][0]
            index = library.index(book)
            before = book.status
            book.status = "В наличии" if book.status == "Выдана" else "Выдана"
            print(f"Статус книги с id: {book.id} изменен с \"{before}\" на \"{book.status}\"")
            library[index] = book
            updated_lib_dict = self._lib_to_dict(library)
            with open(self.STORAGE_PATH, "w", encoding="utf-8") as file:
                json.dump(updated_lib_dict, file, ensure_ascii=False)
        except IndexError:
            print("Такой книги не существует")

    def search_book_by(self, field_name: str, value: str | int) -> list[Book]:
        """
        find by field and return Book objects
        """
        fields = {
            "название": "title",
            "автор": "author",
            "год": "year",
        }
        library = self.get_all_books()
        find_books = []
        for book in library:
            if getattr(book, fields[field_name]) == value:
                find_books.append(book)
        return find_books
