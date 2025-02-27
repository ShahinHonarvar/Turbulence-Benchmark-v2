def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(list_of_integers):
    primes_in_range = [num for idx, num in enumerate(list_of_integers[27:87]) if is_prime(num)]
    return sorted(primes_in_range, reverse=True)