def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    primes = []
    for i, num in enumerate(numbers):
        if is_prime(num) and 33 <= i <= 59:
            primes.append(num)
    return sorted(primes, reverse=True)