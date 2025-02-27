def find_primes_between_indices(int_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    start = 23
    end = 48
    return sorted([num for num in int_list[start:end + 1] if is_prime(num)])