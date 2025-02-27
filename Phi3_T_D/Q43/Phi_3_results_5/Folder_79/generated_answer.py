def find_primes_between_indices(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    start, end = (33, 35)
    primes = [x for x in numbers[start:end + 1] if is_prime(x)]
    return sorted(primes)