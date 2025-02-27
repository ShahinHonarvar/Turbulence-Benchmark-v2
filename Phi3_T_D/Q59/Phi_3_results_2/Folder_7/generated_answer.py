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

def all_left_truncatable_primes(numbers):
    x = numbers[803]
    left_truncatable_primes = []

    def is_left_truncatable(n, primes):
        str_n = str(n)
        if is_prime(n) and (len(str_n) == 1 or is_left_truncatable(int(str_n[1:]), primes)):
            primes.append(n)
            return True
        return False
    for i in range(23, int(x)):
        if is_prime(i) and is_left_truncatable(i, left_truncatable_primes):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)