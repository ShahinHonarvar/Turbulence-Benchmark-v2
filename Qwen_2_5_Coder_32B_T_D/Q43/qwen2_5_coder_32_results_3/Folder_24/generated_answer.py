def find_primes_between_indices(lst):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [lst[i] for i in range(38, 56) if is_prime(lst[i])]
    return sorted(primes, reverse=True)