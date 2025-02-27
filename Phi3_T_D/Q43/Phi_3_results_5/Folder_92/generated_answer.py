def find_primes_between_indices(num_list):
    start, end = (7, 8)
    primes = [num_list[i] for i in range(start, end + 1) if is_prime(num_list[i])]
    return sorted(primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True