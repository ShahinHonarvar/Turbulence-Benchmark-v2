def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_primes(numbers):
    threshold = numbers[97]
    right_truncatable_primes = [num for num in range(2, threshold) if is_prime(num) and all((is_prime(num // 10 ** i) for i in range(int(num ** 0.5) // 10 + 1)))]
    return sorted(right_truncatable_primes, reverse=True)