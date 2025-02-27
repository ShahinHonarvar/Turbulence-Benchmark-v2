def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if int(str_n[i:]) not in primes or int(str_n[:-i]) not in primes:
            return False
    return True

def generate_primes(limit):
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def all_left_right_truncatable_prime(numbers):
    x = numbers[69] if len(numbers) > 69 else 0
    primes = generate_primes(x)
    return sorted([p for p in primes if is_truncatable_prime(p, set(primes))], reverse=True)