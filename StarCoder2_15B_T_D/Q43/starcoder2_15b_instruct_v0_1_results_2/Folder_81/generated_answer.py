def find_primes_between_indices(numbers):
    primes = []
    for i, num in enumerate(numbers):
        if is_prime(num) and 59 <= i <= 97:
            primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True