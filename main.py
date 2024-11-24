from src.app import start_app
from src.commands import welcome_msg


if __name__ == "__main__":
    welcome_msg()
    try:
        start_app()
    except KeyboardInterrupt or EOFError:
        print("\nДо свидания!")
        exit()