def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start_index, end_index = (61, 79)
    primes = [num for i, num in enumerate(lst[start_index:end_index + 1]) if is_prime(num)]
    return sorted(primes)