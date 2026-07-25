"""
Пакет src для проекта EDA Titanic.
Содержит вспомогательные функции для загрузки и обработки данных.
"""

from .data_loader import load_titanic_data

__all__ = [
    'load_titanic_data',
]