from src.Book import Book
from src.User import User


class Library:
    def __init__(self) -> None:
        self.__books: list[str] = []
        self.__users: list[str] = []
        self.__checked_out_books: list[str] = []
        self.__checked_in_books: list[str] = []

    # Getters
    def get_books(self) -> list:
        return self.__books

    def get_users(self) -> list:
        return self.__users

    def get_checked_out_books(self) -> list:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn : str, title: str, author: str) -> None:
        new_book: Book = Book(isbn, title, author)
        for book in self.__books:
            if new_book.__eq__(book):
                pass
        self.__books.append(new_book)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(book.__str__())

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str ) -> str:
        for book in self.__books:
            if book.get_isbn() == isbn:
                for user in self.__users:
                    if user.get_dni() == dni:
                        if book.is_available():
                            book.set_available(False)
                            self.__checked_out_books.append([isbn, dni, due_date])
                            book.increment_checkout_num()
                            user.increment_checkouts()
                            return f"User {dni} checked out book {isbn}"
                        else:
                            return f"Book {isbn} is not available"
        return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        for book in self.__books:
            if book.get_isbn() == isbn:
                for user in self.__users:
                    if user.get_dni() == dni:
                        if not book.is_available():
                            book.set_available(True)
                            self.__checked_in_books.append([isbn, dni, returned_date])
                            for entry in self.__checked_out_books:
                                if entry[0] == isbn and entry[1] == dni:
                                    self.__checked_out_books.remove(entry)
                            user.increment_checkins()
                            return f"Book {isbn} checked in by user {dni}"
                        else:
                            return f"Book {isbn} is not available"
        return f"Book {isbn} is not available"


    # Utils
    def add_user(self, dni: int, name: str) -> None:
        new_user = User(dni, name)
        self.__users.append(new_user)
