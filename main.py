import os
from wallet import Wallet
from typing import List, Dict, Union


def main_menu() -> None:
    """
    Выводит главное меню приложения
    """
    print("\nГлавное меню:")
    print("1. Посмотреть баланс")
    print("2. Добавить транзакцию")
    print("3. Редактировать транзакцию")
    print("4. Поиск транзакции")
    print("5. Выход")


def exit_menu() -> None:
    """
    Выводит меню выхода или возврата в главное меню. Срабатывает после заканчиваний действий в каждом блоке
    """
    print("\n1. Вернуться в меню")
    print("2. Выход")

    choice: str = input("Выберите номер действия: ")
    if choice == "1":
        os.system("cls||clear")

    elif choice == "2":
        print("Выход из программы...")
        exit()

    else:
        print("Некорректный выбор. Пожалуйста, введите номер действия из меню.")
        exit_menu()


def view_balance(wallet: Wallet) -> None:
    """
    Отображает текущий баланс кошелька

    :param wallet: Экземпляр класса кошелька
    """
    balance: float = wallet.get_balance()
    print("\nТекущий баланс: ", balance)


def view_transaction(transaction: Dict[str, Union[str, float]]) -> None:
    """
    Отображает транзакцию

    :param transaction: транзакция из transactions json-файла
    """
    print(f'Дата: {transaction["date"]}')
    print(f'Категория: {transaction["category"]}')
    print(f'Сумма: {transaction["amount"]}')
    print(f'Описание: {transaction["description"]}')


def add_transaction(wallet: Wallet) -> None:
    """
    Добавляет новую транзакцию в кошелёк

    :param wallet: Экземпляр класса кошелька
    """
    print("\nДобавление новой транзакции")
    category: str = input("Введите категорию (Расход/Доход): ").capitalize()
    amount: float = float(input("Введите сумму транзакции: "))
    description: str = input("Введите описание: ").capitalize()
    wallet.add_transaction(category, amount, description)
    print("Транзакция успешно добавлена")


def edit_transaction(wallet: Wallet) -> None:
    """
    Редактирует выбранную пользователем транзакцию.

    :param wallet: Экземпляр класса кошелька
    """
    print("\nДавайте найдем транзакцию для редактирования")
    search_transactions(wallet)

    choice: int = int(input("\nВведите номер транзакции, которую хотели бы отредактировать: "))
    view_transaction(temp[choice - 1])

    date: str = input('Введите новую дату (пример: ДД-ММ-ГГГГ) ((если желаете оставить прежнюю - оставьте строку пустой)): ')
    category: str = input("Введите новую категорию (Расход/Доход) ((если желаете оставить прежнюю - оставьте строку пустой)): ").capitalize()
    amount: str = input("Введите новую сумму (если желаете оставить прежнюю - оставьте строку пустой): ")
    description: str = input("Введите новое описание (если желаете оставить прежнее - оставьте строку пустой): ").capitalize()

    wallet.edit_transaction(temp[choice - 1], date, category, amount, description)


def search_transactions(wallet: Wallet) -> None:
    """
    Осуществляет поиск транзакций по различным атрибутам.

    :param wallet: Экземпляр класса кошелька
    """


    global temp #Temp - массив, в котором содержатся транзакции, которые будут выведены пользователю. Нужен для функции редактирования

    print("Введите номер атрибута, по которому хотите осуществить поиск")
    print("1. Дата")
    print("2. Категория")
    print("3. Сумму")
    print("4. Все транзакции")
    choice: str = input("Номер атрибута: ")
    if choice == "1":
        date: str = input("Введите дату (пример: ДД-ММ-ГГГГ): ")
        dates: List[Dict[str, Union[str, float]]] = wallet.get_transactions_by_date(date)
        temp = dates
        for date in dates:
            print(f'{dates.index(date) + 1})')
            view_transaction(date)

    if choice == "2":
        category: str = input("Введите категорию: ")
        categories: List[Dict[str, Union[str, float]]] = wallet.get_transactions_by_category(category.capitalize())
        temp = categories
        for category in categories:
            print(f'{categories.index(category) + 1})')
            view_transaction(category)

    if choice == "3":
        amount: float = float(input("Введите сумму: "))
        amounts: List[Dict[str, Union[str, float]]] = wallet.get_transactions_by_amount(amount)
        temp = amounts
        for amount in amounts:
            print(f'{amounts.index(amount) + 1})')
            view_transaction(amount)

    if choice == "4":
        transactions: List[Dict[str, Union[str, float]]] = wallet.get_transactions()
        temp = transactions
        for transaction in transactions:
            print(f'{transactions.index(transaction) + 1})')
            view_transaction(transaction)


def main() -> None:
    """
    Основная функция приложения. Запускает главное меню и обрабатывает выбор пользователя.
    """

    wallet: Wallet = Wallet("wallet_data.json")

    while True:
        main_menu()
        choice: str = input("Выберите номер действия: ")

        if choice == "1":
            view_balance(wallet)
            exit_menu()

        elif choice == "2":
            add_transaction(wallet)
            exit_menu()

        elif choice == "3":
            os.system('cls||clear')
            edit_transaction(wallet)
            exit_menu()

        elif choice == "4":
            os.system('cls||clear')
            search_transactions(wallet)
            exit_menu()

        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите номер действия из меню.")


if __name__ == '__main__':
    main()
