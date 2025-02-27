def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for i, num in enumerate(numbers):
        if is_prime(num) and 43 <= i <= 76:
            primes.append(num)
    return sorted(primes, reverse=True)