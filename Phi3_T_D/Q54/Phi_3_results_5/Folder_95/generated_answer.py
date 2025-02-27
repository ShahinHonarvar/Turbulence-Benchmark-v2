def is_prime(n):
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[77]
    right_truncatable_primes = []

    def is_right_truncatable(n):
        original = n
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for number in range(2, x):
        if is_right_truncatable(number):
            right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes)