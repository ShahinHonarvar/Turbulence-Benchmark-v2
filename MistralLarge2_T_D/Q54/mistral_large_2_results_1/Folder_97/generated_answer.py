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

def generate_right_truncatable_primes(limit):
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    right_truncatable_primes = []
    for prime in primes:
        temp = prime
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            right_truncatable_primes.append(prime)
    return right_truncatable_primes

def all_right_truncatable_prime(tup):
    x = tup[645]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    return sorted(right_truncatable_primes)