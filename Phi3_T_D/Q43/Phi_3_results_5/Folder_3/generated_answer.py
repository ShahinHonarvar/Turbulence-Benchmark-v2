def find_primes_between_indices(num_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = sorted((n for n in num_list[80:85] if is_prime(n)), reverse=True)
    return primes