def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncatable_primes(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        original_prime = prime
        while original_prime > 0:
            if not is_prime(original_prime):
                break
            truncatable_primes.append(prime)
            original_prime //= 10
    return sorted(set(truncatable_primes[1:]), reverse=True)

def all_right_truncatable_prime(numbers):
    if len(numbers) < 1046:
        return []
    x = numbers[945]
    return right_truncatable_primes(x)