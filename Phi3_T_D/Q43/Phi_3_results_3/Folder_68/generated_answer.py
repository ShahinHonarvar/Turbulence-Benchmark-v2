def find_primes_between_indices(lst):

    def is_prime(num):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        return False
    return sorted([x for x in lst[1:6] if is_prime(x)])