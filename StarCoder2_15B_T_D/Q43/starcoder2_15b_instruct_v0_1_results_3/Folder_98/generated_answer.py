def find_primes_between_indices(numbers):

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    primes = []
    for i, number in enumerate(numbers):
        if is_prime(number) and i >= 1 and (i <= 2):
            primes.append(number)
    return sorted(primes, reverse=True)