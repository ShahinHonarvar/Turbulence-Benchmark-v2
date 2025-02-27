def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    start_index = 61
    end_index = 80
    primes = [num for num in lst[start_index:end_index + 1] if is_prime(num)]
    return sorted(primes, reverse=True)