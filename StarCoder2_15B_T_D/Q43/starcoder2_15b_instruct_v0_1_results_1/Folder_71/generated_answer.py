def find_primes_between_indices(numbers):
    primes = [num for num in numbers[57:65] if is_prime(num)]
    primes.sort(reverse=True)
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True