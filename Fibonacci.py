def fibonacci(n: int) -> int:
    """
    Рекурсия(оптимально до n < 35)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def bine(n: int) -> float:
    """
    По формуле Бине(работает до n < 1475)
    через модуль decimal можно расширить ограничение n
    """
    phi = ((1 + 5 ** 0.5) / 2)
    return ((phi ** n) - ((-phi) ** -n)) / 5 ** 0.5


if __name__ == '__main__':
    f = bine(1474)
    print(f)
