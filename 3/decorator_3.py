import functools
from datetime import datetime


def logger(path):
    def decorator(old_function):
        @functools.wraps(old_function)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()  # Записываем время начала выполнения функции
            result = old_function(*args, **kwargs)
            duration = datetime.now() - start_time  # Вычисляем продолжительность выполнения
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(f'{datetime.now()} - Вызвана функция: {old_function.__name__}\n')
                log_file.write(f'Аргументы: позиционные - {args}; ключевые - {kwargs}\n')
                log_file.write(f'Результат: {result}\n')
                log_file.write(f'Время выполнения: {duration}\n\n')  # Добавляем время выполнения в лог
            return result
        return wrapper
    return decorator
