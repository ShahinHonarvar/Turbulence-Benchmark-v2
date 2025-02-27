def find_primes_between_indices(list_of_ints):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for num in list_of_ints if is_prime(num)]
    return sorted(primes[0:2])