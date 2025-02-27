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

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    right_truncatable_primes = []

    def is_right_truncatable(prime_candidate):
        str_prime = str(prime_candidate)
        while len(str_prime) > 1:
            if not is_prime(int(str_prime)):
                return False
            str_prime = str_prime[:-1]
        return True
    for num in range(x - 1, 1, -1):
        if is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return right_truncatable_primes