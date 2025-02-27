def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(numbers):
    result = []
    x = numbers[767]
    for i in range(x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)