def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(prime):
    return all((is_prime(int(prime[:i])) for i in range(1, len(str(prime)))))

def all_right_truncatable_primes(numbers):
    x = numbers[52]
    right_truncatable_primes = []
    for num in range(x - 1, 7, -1):
        if is_prime(num) and is_right_truncatable(num):
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)