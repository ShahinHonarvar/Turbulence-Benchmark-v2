def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index = 70
    end_index = 71
    primes = []
    for i, n in enumerate(numbers):
        if is_prime(n) and start_index <= i <= end_index:
            primes.append(n)
    return sorted(primes, reverse=True)