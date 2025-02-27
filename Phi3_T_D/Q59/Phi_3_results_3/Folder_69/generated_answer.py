def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def backtrack(number, primes, x):
    if number > x or not number:
        return
    if is_prime(number):
        primes.append(number)
    backtrack(number // 10, primes, x)

def all_left_truncatable_prime(numbers):
    x = numbers[760]
    primes = []
    backtrack(x, primes, x)
    return sorted(primes, reverse=True)