def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            if all((is_prime(int(str(num)[:i])) for i in range(1, len(str(num))))):
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True