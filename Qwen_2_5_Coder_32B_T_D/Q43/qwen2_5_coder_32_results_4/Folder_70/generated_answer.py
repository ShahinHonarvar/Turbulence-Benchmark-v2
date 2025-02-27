def find_primes_between_indices(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [numbers[i] for i in range(max(0, 131), min(len(numbers), 816)) if is_prime(numbers[i])]
    return sorted(primes, reverse=True)