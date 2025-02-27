def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(arr):
    if len(arr) < 735:
        raise ValueError('List is too short. It must have at least 735 elements.')
    primes = [num for num in arr[156:735] if is_prime(num)]
    return sorted(primes, reverse=True)