def find_primes_between_indices(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_sublist_primes(start, end):
        return sorted([num for num in lst[start:end + 1] if is_prime(num)])
    return get_sublist_primes(46, 61)