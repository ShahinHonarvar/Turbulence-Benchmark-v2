def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, truncatable_history):
    str_n = str(n)
    if not all((c in '123456789' for c in str_n)):
        return False
    if n in truncatable_history:
        return False
    truncatable_history.add(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[77]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n, set())]
    return truncatable_primes