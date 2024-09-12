# from typing import Self


class Book:
    def __init__(self, isbn: str, title: str, author: str, available: bool = True, checkout_num: int = 0) -> None:
        self.__isbn: str = isbn
        self.__title: str = title
        self.__author: str = author
        self.__available: bool = available
        self.__checkout_num: int = checkout_num

    # Getters
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def get_checkout_num(self):
        return self.__checkout_num

    # Setters
    def set_available(self, available: bool) -> None:
        self.__available = available

    def increment_checkout_num(self) -> None:
        self.__checkout_num += 1

    # Utils
    def __str__(self) -> str:
        return f"ISBN: {self.__isbn}, Title: {self.__title}, Author: {self.__author}"


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book): #checks if other's class is 'Book' or not
            return False
        return other.get_isbn() == self.__isbn #checks if other's isbn is already in the library


