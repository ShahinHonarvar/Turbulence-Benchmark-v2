def all_right_truncatable_prime(numbers):
    if numbers[0] < 11:
        return []
    primes = [2, 3, 5, 7]
    right_truncatable_primes = set(range(11, numbers[0]))
    for num in right_truncatable_primes:
        if not all((num % p for p in primes)) or not num % 10 in (1, 3, 7, 9):
            right_truncatable_primes.remove(num)
    return sorted(list(right_truncatable_primes), reverse=True)