import json
from datetime import datetime
from typing import List, Dict, Union


class Wallet:
    def __init__(self, file_path: str) -> None:
        """
        Инициализирует кошелек.
        :param file_path: Путь к файлу, в котором хранятся данные о транзакциях
        """
        self.file_path: str = file_path
        self.data: Dict[str, List[Dict[str, Union[str, float]]]] = self.load_data()

    def load_data(self) -> Dict[str, List[Dict[str, Union[str, float]]]]:
        """
        Загружает данные о транзакциях из файла
        :return: В случае существования файла загружает данные из файла, в противном возвращает пустой словарь транзакций
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {'transactions': []}

    def save_data(self) -> None:
        """
        Сохраняет данные о транзакциях в файл
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file)

    def add_transaction(self, category: str, amount: float, description: str='') -> None:
        """
        Добавляет новую транзакцию в кошелек
        :param category: Категория транзакции (Расход/Доход)
        :param amount: Сумма транзакции
        :param description: Описание транзакции
        """
        transactions: Dict[str, Union[str, float]] = {
            'date': datetime.today().strftime('%d-%m-%Y'),
            'category': category,
            'amount': amount,
            'description': description
        }
        self.data['transactions'].append(transactions)
        self.save_data()

    def edit_transaction(self, transaction: Dict[str, Union[str, float]], date: str=None, category: str=None, amount: float=None, description: str=None) -> None:
        """
        Редактирует существующую транзакцию.
        :param transaction: Транзакция, которую нужно отредактировать
        :param date: Новая дата транзакции
        :param category: Новая категория транзакции
        :param amount: Новая сумма транзакции
        :param description: Новое описание транзакции
        :return:
        """
        if date:
            transaction["date"] = datetime.strptime(date, '%d-%m-%Y').strftime('%d-%m-%Y')
        if category:
            transaction["category"] = category
        if amount:
            transaction["amount"] = float(amount)
        if description:
            transaction["description"] = description
        self.save_data()

    def get_balance(self) -> float:
        """
        Возвращает текущий баланс кошелька
        :return: Текущий баланс кошелька
        """
        income: float = sum(transaction['amount'] for transaction in self.data['transactions'] if transaction['category'] == 'Доход')
        expense: float = sum(transaction['amount'] for transaction in self.data['transactions'] if transaction['category'] == 'Расход')
        balance: float = income - expense
        return balance

    def get_transactions(self) -> List[Dict[str, Union[str, float]]]:
        """
        Возвращает все транзакции из кошелька
        :return: Список словарей, содержащих информацию о транзакциях
        """
        return [transaction for transaction in self.data["transactions"]]

    def get_transactions_by_date(self, date: str) -> List[Dict[str, Union[str, float]]]:
        """
        Возвращает все транзакции, совершенные в указанную дату
        :param: date: Дата транзакции
        :return: Список словарей, содержащих информацию о транзакциях
        """
        return [transaction for transaction in self.data['transactions'] if transaction['date'] == date]

    def get_transactions_by_category(self, category: str) -> List[Dict[str, Union[str, float]]]:
        """
        Возвращает все транзакции указанной категории
        :param category: Категория транзакций
        :return: Список словарей, содержащих информацию о транзакциях
        """
        return [transaction for transaction in self.data['transactions'] if transaction['category'] == category]

    def get_transactions_by_amount(self, amount: float) -> List[Dict[str, Union[str, float]]]:
        """
        Возвращает все транзакции с указанной суммой
        :param amount: Сумма транзакции
        :return: Список словарей, содержащих информацию о транзакциях
        """
        return [transaction for transaction in self.data['transactions'] if transaction['amount'] == amount]
