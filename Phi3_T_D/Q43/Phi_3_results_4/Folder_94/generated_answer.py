def find_primes_between_indices(int_list):

    def is_prime(n):
        if n <= 1 or (n > 2 and n % 2 == 0):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    start_index, end_index = (10, 12)
    primes = [n for n in int_list[start_index:end_index + 1] if is_prime(n)]
    return sorted(primes)