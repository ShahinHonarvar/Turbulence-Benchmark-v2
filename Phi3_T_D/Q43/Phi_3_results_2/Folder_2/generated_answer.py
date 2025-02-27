def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(int_list):
    primes = [item for item in int_list[166:785] if is_prime(item)]
    return sorted(primes, reverse=True)