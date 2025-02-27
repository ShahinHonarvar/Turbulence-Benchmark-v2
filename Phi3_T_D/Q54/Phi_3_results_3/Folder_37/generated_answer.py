def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_right_truncatable(prime, primes_set):
    while prime > 0:
        if prime not in primes_set:
            return False
        prime //= 10
    return True

def get_right_truncatable_primes(threshold):
    right_truncatable_primes = []
    for num in range(11, threshold, 2):
        if is_prime(num) and is_right_truncatable(num, right_truncatable_primes):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)

def all_right_truncatable_prime(numbers):
    x = numbers[35]
    if not isinstance(x, int) or x <= 2:
        return []
    return get_right_truncatable_primes(x)