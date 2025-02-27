def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, d, primes):
    primes.add(n)
    while n > 0:
        if not is_prime(int(str(n)[:d])) or int(str(n)[:d]) in primes:
            return False
        n = int(str(n)[d:])
        d -= 1
    return True

def all_left_truncatable_prime(numbers):
    five_four_index = 54
    x = numbers[five_four_index]
    primes = set()
    left_truncatable_primes = []
    for number in range(2, x):
        if number in primes:
            continue
        if not is_prime(number):
            continue
        if is_left_truncatable_prime(number, len(str(number)), primes):
            left_truncatable_primes.append(number)
    return left_truncatable_primes