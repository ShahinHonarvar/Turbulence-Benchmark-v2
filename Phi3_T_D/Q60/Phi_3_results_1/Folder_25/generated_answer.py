def is_prime(n):
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

def is_truncatable_prime(n, prime_set):
    str_n = str(n)
    for i in range(1, len(str_n) - 1):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    prime_set = set()
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_set.add(i)
            if is_truncatable_prime(i, prime_set):
                truncatable_primes.append(i)
    return truncatable_primes