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

def all_left_right_truncatable_prime(t):
    x = t[14]
    truncatable_primes = []

    def is_truncatable(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        while len(n_str) > 1:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[1:-1]
        return is_prime(int(n_str))
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)