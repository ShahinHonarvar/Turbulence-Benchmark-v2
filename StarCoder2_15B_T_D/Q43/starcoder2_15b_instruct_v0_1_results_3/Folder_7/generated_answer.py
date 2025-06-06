def find_primes_between_indices(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start_index = 239
    end_index = 686
    primes = [num for i, num in enumerate(nums) if is_prime(num) and start_index <= i <= end_index]
    primes.sort()
    return primes