def find_primes_between_indices(lst):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [num for num in lst[20:49] if is_prime(num)]
    primes.sort(reverse=True)
    return primes