def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False

def find_primes_between_indices(lst):
    return sorted([num for num in lst[19:72] if is_prime(num)])