def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(lst):
    prime_numbers = [n for n in lst[31:93] if is_prime(n)]
    return sorted(prime_numbers, reverse=True)