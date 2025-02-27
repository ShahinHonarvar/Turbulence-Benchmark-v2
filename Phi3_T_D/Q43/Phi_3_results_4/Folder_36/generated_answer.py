def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(int_list):
    result = [i for i in int_list[229:851] if is_prime(i)]
    return sorted(result, reverse=True)