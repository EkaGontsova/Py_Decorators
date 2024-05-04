from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(f'{datetime.now()} - Вызвана функция: {old_function.__name__}\n')
                log_file.write(f'Аргументы: позиционные - {args}; ключевые - {kwargs}\n')
                log_file.write(f'Результат: {result}\n\n')
            return result
        return new_function
    return __logger
