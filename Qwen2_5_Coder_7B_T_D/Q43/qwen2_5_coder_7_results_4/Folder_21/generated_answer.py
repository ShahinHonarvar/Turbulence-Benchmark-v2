def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_between_indices(numbers):
    primes = []
    for i in range(239, 687):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    primes.sort()
    return primes