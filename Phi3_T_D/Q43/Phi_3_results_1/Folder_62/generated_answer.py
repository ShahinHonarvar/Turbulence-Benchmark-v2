def find_primes_between_indices(num_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for ix, num in enumerate(num_list[29:98]) if is_prime(num)]
    primes.sort(reverse=True)
    return primes