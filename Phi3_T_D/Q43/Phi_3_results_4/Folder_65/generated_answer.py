def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(int_list):
    primes_in_range = [element for element in int_list[75:93] if is_prime(element)]
    return sorted(primes_in_range)