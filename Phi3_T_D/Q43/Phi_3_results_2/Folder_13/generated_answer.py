def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start_index = 415
    end_index = 647
    primes = [n for n in lst[start_index:end_index + 1] if is_prime(n)]
    return sorted(primes)