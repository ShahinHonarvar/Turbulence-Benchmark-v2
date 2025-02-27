def find_primes_between_indices(int_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    start_index = max(14, min(73, len(int_list) - 1))
    primes = [num for num in int_list[start_index:74] if is_prime(num)]
    return sorted(primes, reverse=True)