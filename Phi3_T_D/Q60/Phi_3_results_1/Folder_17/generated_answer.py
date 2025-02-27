def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_and_right_truncatable_prime(n, primes):
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[36] if len(numbers) > 36 else None
    if x is None or x <= 11:
        return []
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_and_right_truncatable_prime(num, [2, 3, 5, 7]):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)