def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n: int) -> bool:
    original_n = n
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return original_n > 0

def all_left_truncatable_prime(numbers: tuple) -> list:
    x = numbers[126]
    result = []
    for num in range(x - 1, 11, -1):
        if is_left_truncatable_prime(num):
            result.append(num)
    return result