def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n) - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[90] if len(numbers) > 90 else None
    if x is None:
        return []
    truncatable_primes = [2, 3, 5, 7]
    for i in range(11, x + 1):
        if is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)