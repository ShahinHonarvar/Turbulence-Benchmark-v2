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

def find_primes_between_indices(numbers_list):
    start_idx = 424
    end_idx = 552
    primes_in_range = [num for idx, num in enumerate(numbers_list[start_idx:end_idx + 1], start_idx) if is_prime(num)]
    return sorted(primes_in_range, reverse=True)