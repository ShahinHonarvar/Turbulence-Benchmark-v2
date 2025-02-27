def find_primes_between_indices(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    start, end = (261, 459)
    return sorted([num for i, num in enumerate(numbers) if is_prime(num) and start <= i <= end])