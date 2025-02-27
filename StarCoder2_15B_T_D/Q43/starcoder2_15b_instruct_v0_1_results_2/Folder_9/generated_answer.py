def find_primes_between_indices(numbers):
    start_index = 16
    end_index = 71
    primes = []
    for i, num in enumerate(numbers):
        if i < start_index:
            continue
        if i > end_index:
            break
        if is_prime(num):
            primes.append(num)
    primes.sort()
    return primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True