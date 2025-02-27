def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = []
    for idx, num in enumerate(numbers):
        if is_prime(num) and 55 <= idx <= 76:
            primes.append(num)
    return sorted(primes)