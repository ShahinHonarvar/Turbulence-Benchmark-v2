def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [n for n in nums if is_prime(n)]
    primes_in_range = primes[6:8]
    primes_in_range.sort(reverse=True)
    return primes_in_range