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

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[43]
    truncatable_primes = []
    for num in range(23, x + 1):
        if is_prime(num):
            s = str(num)
            if all((is_prime(int(s[i:])) and is_prime(int(s[:i + 1])) for i in range(len(s) - 1))):
                truncatable_primes.append(num)
    return truncatable_primes