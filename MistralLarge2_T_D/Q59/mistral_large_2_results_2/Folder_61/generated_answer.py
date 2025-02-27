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

def all_left_truncatable_prime(t):
    x = t[3]

    def is_left_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
        return True
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)