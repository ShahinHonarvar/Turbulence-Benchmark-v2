def find_primes_between_indices(numbers):
    primes_in_range = []
    for i in range(min(len(numbers), 3)):
        if is_prime(numbers[i]):
            primes_in_range.append(numbers[i])
    return sorted(primes_in_range, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True