def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = []
    for i, n in enumerate(numbers):
        if is_prime(n) and 131 <= i <= 815:
            prime_numbers.append(n)
    return sorted(prime_numbers, reverse=True)