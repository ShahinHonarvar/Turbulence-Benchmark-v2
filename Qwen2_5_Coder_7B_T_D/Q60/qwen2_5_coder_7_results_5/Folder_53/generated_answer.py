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

def is_left_right_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
        if not is_prime(int(n_str[:len(n_str) - i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = [p for p in primes if is_left_right_truncatable_prime(p)]
    return sorted(left_right_truncatable_primes, reverse=True)