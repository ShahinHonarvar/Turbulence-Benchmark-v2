def find_primes_between_indices(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for index, num in enumerate(numbers) if 16 <= index <= 71 and is_prime(num)]
    return sorted(primes)