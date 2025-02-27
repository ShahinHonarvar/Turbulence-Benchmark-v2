def find_primes_between_indices(numbers):

    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    primes = [number for number in numbers[33:60] if is_prime(number)]
    return sorted(primes, reverse=True)