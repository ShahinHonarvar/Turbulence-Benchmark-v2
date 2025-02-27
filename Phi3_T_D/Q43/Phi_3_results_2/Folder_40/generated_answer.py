def find_primes_between_indices(integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [num for num in integers[1:2] if is_prime(num)]
    return sorted(primes)