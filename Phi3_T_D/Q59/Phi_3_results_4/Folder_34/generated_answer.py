def is_left_truncatable_prime(n, prime_list):
    while n:
        if not is_prime(n):
            return False
        n = n // 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[18]
    primes = [2, 3, 5, 7]
    for i in range(11, x, 2):
        if is_prime(i):
            if is_left_truncatable_prime(i, primes):
                primes.append(i)
    return sorted(primes, reverse=True)