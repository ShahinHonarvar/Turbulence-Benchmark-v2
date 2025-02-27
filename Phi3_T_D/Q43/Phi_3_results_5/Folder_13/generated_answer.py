def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(int_list):
    result = [num for num in int_list[415:648] if is_prime(num)]
    return sorted(result)