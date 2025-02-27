def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, prime_list):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if is_prime(int(str_n[i:])) is False or is_prime(int(str_n[:i])) is False:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    for i in range(11, max(numbers), 2):
        if is_prime(i):
            primes.append(i)
    x = numbers[175]
    return sorted([p for p in primes if p <= x and is_truncatable_prime(p, primes)])