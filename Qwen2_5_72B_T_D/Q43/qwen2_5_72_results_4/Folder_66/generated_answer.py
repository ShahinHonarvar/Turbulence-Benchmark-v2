def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if 72 < 0 or 72 >= len(numbers):
        return []
    primes = []
    if is_prime(numbers[72]):
        primes.append(numbers[72])
    return sorted(primes)