def find_primes_between_indices(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    filtered_primes = [num for idx, num in enumerate(lst[18:86], start=19) if is_prime(num)]
    return sorted(filtered_primes, reverse=True)