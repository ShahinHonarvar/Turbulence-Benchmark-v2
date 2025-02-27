def find_primes_between_indices(arr):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    primes_in_range = [x for i, x in enumerate(arr[239:686]) if is_prime(x)]
    return primes_in_range