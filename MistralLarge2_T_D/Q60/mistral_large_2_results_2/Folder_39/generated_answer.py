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

def all_left_right_truncatable_prime(numbers):
    x = numbers[30]

    def is_left_right_truncatable(n):
        if not is_prime(n):
            return False
        n_str = str(n)
        if '0' in n_str:
            return False
        while len(n_str) > 1:
            n_str = n_str[1:-1]
            if not n_str or not is_prime(int(n_str)):
                return False
        return True
    truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable(n)]
    return sorted(truncatable_primes, reverse=True)