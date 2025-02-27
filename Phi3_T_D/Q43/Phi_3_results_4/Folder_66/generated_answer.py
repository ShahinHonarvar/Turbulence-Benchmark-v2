def is_prime(num):
    if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
        return True
    return False

def find_primes_between_indices(lst):
    start_index = 72
    end_index = 72
    return sorted([x for x in lst[start_index:end_index + 1] if is_prime(x)])