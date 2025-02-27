def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    from_index = 1 * 112
    to_index = 3 * 61 + 1
    primes = [num for num in lst[from_index:to_index + 1] if is_prime(num)]
    return sorted(primes, reverse=True)