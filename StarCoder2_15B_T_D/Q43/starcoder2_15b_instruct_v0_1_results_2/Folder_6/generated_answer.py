def find_primes_between_indices(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index = 89
    end_index = 93
    primes = []
    for i, num in enumerate(numbers):
        if is_prime(num) and start_index <= i <= end_index:
            primes.append(num)
    return sorted(primes, reverse=True)