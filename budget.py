from __future__ import annotations

from typing import Mapping, List

import math

Ledger = List[Mapping[str, any]]


class Category:
    def __init__(self, name: str):
        self.name: str = name
        self.ledger: Ledger = []
        self._funds: float = 0

    def deposit(self, amount: float, description: str = '') -> None:
        self._funds += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount: float, description: str = '') -> bool:
        if not self.check_funds(amount):
            return False

        self._funds -= amount
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self) -> float:
        return self._funds

    def check_funds(self, amount: float) -> bool:
        return amount <= self._funds

    def transfer(self, amount: float, other: Category) -> None:
        if not self.check_funds(amount):
            return False

        self._funds -= amount
        self.ledger.append({'amount': -amount, 'description': f'Transfer to {other.name}'})
        other.deposit(amount, f'Transfer from {self.name}')
        return True

    def __str__(self):
        output = ''
        number_of_stars = 30 - len(self.name)
        start_padding = math.floor(number_of_stars / 2)
        end_padding = math.ceil(number_of_stars / 2)
        output += f'{"*" * start_padding}{self.name}{"*" * end_padding}\n'

        for entry in self.ledger:
            description: str = entry['description'] if len(entry['description']) < 23 else entry['description'][:23]
            description = description.ljust(23, ' ')
            amount = f'{entry["amount"]:.2f}'
            output += f'{description} {amount}\n'

        output += f'Total: {self.get_balance()}'
        return output


def create_spend_chart(categories: List[Category]) -> str:
    pass
