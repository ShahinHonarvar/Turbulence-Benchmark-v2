def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_right_truncatable_primes(limit):
    primes = [2, 3, 5, 7]
    for p in primes:
        if p < limit:
            for digit in '1379':
                new_prime = int(str(p) + digit)
                if is_prime(new_prime):
                    primes.append(new_prime)
    return sorted(set(primes))

def all_right_truncatable_prime(numbers):
    x = numbers[758]
    return [p for p in generate_right_truncatable_primes(x) if p < x]