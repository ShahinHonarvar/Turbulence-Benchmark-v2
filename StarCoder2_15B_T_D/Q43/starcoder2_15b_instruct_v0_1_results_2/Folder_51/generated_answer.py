def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start_index = 14
    end_index = 68
    primes = [num for i, num in enumerate(lst) if start_index <= i <= end_index and is_prime(num)]
    primes.sort(reverse=True)
    return primes