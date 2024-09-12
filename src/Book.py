# from typing import Self


class Book:
    def __init__(self, isbn, title, author, available=True, checkout_num=0):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__available = available
        self.__checkout_num = checkout_num

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
    def set_available(self, available: bool):
        self.__available = available

    def increment_checkout_num(self):
        self.__checkout_num += 1

    # Utils
    def __str__(self) -> str:
        return f"ISBN: {self.__isbn}, Title: {self.__title}, Author: {self.__author}"


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book): #checks if other's class is 'Book' or not
            return False
        return other.get_isbn() == self.__isbn #checks if other's isbn is already in the library


