import json
import os

from src.books_repository import BookRepository
from src.models import Book

repo = BookRepository()

book = Book(1, "Test Book", "Test Author", 2024, "В наличии")

books_data = [
  {"id": 1, "title": "Грокаем алгоритмы.", "author": "Бхаргава А.", "year": 2024, "status": "В наличии"},
  {"id": 2, "title": "Думай как математик", "author": "Barbara Oakley", "year": 2014, "status": "В наличии"},
  {"id": 3, "title": "Python. К вершинам мастерства.", "author": "Лусиану Рамальо", "year": 2022, "status": "Выдана"}
]


def test_get_all_books_empty():
    """
    create empty file and check if is empty
    """
    repo.STORAGE_PATH = "test_library.json"
    open(repo.STORAGE_PATH, "w").close()  # Создаем пустой файл
    books = repo.get_all_books()
    assert books == [], "Test failed: get_all_books should return an empty list for an empty file"
    os.remove(repo.STORAGE_PATH)


def test_add_book():
    """
    add book and check if is added
    """
    repo.STORAGE_PATH = "test_library.json"
    repo.add_book(book)
    with open(repo.STORAGE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    os.remove(repo.STORAGE_PATH)

    assert len(data) == 1, "Test failed: Book was not added"
    assert data[0]["title"] == "Test Book", "Test failed: Book title mismatch"


def test_get_next_id():
    """
    check if method get_next_id() return 'last_id + 1'
    """
    repo.STORAGE_PATH = "test_library.json"
    with open(repo.STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(books_data, f)
    next_id = repo.get_next_id()
    os.remove(repo.STORAGE_PATH)

    assert next_id == 4, "Test failed: get_next_id did not return the correct value"


def test_delete_book():
    """
    check delete of book from storage
    """
    repo.STORAGE_PATH = "test_library.json"
    with open(repo.STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(books_data, f)

    repo.delete_book(1)
    with open(repo.STORAGE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    os.remove(repo.STORAGE_PATH)

    assert len(data) == 2, "Test failed: Book was not deleted"
    assert data[0]["id"] == 2, "Test failed: Incorrect book was deleted"


def test_book_status_change():
    """
    add books, change status of one and check statuses in library
    """
    repo.STORAGE_PATH = "test_library.json"
    with open(repo.STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(books_data, f)

    repo.book_status_change(1)
    with open(repo.STORAGE_PATH, "r", encoding="utf-8") as f:
        updated_data = json.load(f)
    os.remove(repo.STORAGE_PATH)

    assert updated_data[0]["status"] == "Выдана", "Test failed: Book status was not changed correctly"
    assert updated_data[1]["status"] == "В наличии", "Test failed: Other book status was incorrectly changed"


def test_search_book_by():
    """
    add 3 books and check different options of seacrch
    """
    repo.STORAGE_PATH = "test_library.json"
    with open(repo.STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(books_data, f)

    result_by_title = repo.search_book_by("название", "Book 1")
    result_by_author = repo.search_book_by("автор", "Author 2")
    result_by_year = repo.search_book_by("год", 2022)
    os.remove(repo.STORAGE_PATH)

    assert len(result_by_title) == 2, "Test failed: Incorrect number of books found by title"
    assert result_by_title[0].author == "Author 1", "Test failed: Incorrect book found by title"
    assert len(result_by_author) == 1, "Test failed: Incorrect number of books found by author"
    assert result_by_author[0].title == "Book 2", "Test failed: Incorrect book found by author"
    assert len(result_by_year) == 1, "Test failed: Incorrect number of books found by year"
    assert result_by_year[0].author == "Author 3", "Test failed: Incorrect book found by year"


def run_tests():
    test_get_all_books_empty()
    test_add_book()
    test_get_next_id()
    test_delete_book()
    test_book_status_change()
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
