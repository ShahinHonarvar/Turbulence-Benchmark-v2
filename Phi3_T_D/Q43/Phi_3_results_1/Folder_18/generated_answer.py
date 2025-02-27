def find_primes_between_indices(arr):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes_in_range = [number for number in arr[430:806] if is_prime(number)]
    return sorted(primes_in_range)