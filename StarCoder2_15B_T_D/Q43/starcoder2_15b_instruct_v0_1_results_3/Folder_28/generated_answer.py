def find_primes_between_indices(nums):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i, num in enumerate(nums):
        if is_prime(num) and 38 <= i <= 54:
            primes.append(num)
    primes.sort(reverse=True)
    return primes