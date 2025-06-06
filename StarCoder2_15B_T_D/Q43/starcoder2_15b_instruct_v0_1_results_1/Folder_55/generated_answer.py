def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for i, num in enumerate(numbers):
        if is_prime(num) and 2 <= i <= 2:
            primes.append(num)
    primes.sort()
    return primes