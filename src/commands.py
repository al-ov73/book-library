from src.config import book_repository
from src.models import Book, STATUS

COMMANDS = [
    "Добавить",
    "Удалить",
    "Поиск",
    "Все",
    "Изменить"
]

def welcome_msg() -> None:
    print("Добро пожаловать в нашу библиотеку!")
    print("Доступные команды (в любом регистре):")
    for index, command in enumerate(COMMANDS):
        print(f"{index}. {command}")
    print("Чтобы выйти, нажмите Ctrl+C")

def start_command() -> str:
    command = input("Введите команду: ")
    return command

def wrong_command() -> None:
    print("Некорректная команда")
    print("Попробуйте еще раз")
    
def add_book_command() -> Book:
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год издания книги: ")
    id = book_repository.get_next_id()
    return Book(
        id=id,
        title=title,
        author=author,
        year=int(year),
        status=STATUS.stock.value,
    )

def delete_command() -> int:
    book_id = input("Введите id книги, которую хотите удалить: ")
    return int(book_id)

def book_issue_command() -> int:
    book_id = input("Введите id книги, у которой хотите поменять статус: ")
    return int(book_id)

def book_search_command() -> tuple[str]:
    field = input("Введите поле, по которому ищем (название, автор, год): ")
    value = input("Введите значение: ")
    if field == "год":
        value = int(value)
    return field, value