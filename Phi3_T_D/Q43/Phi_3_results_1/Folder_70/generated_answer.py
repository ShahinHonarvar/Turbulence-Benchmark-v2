def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [num for num in numbers[130:815] if is_prime(num)]
    primes.sort(reverse=True)
    return primes