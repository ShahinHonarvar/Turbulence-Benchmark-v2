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

def truncatable_primes(prime_digits):
    results = []
    for prime in prime_digits:
        prime_str = str(prime)
        for i in range(1, len(prime_str)):
            if not is_prime(int(prime_str[i:])) or not is_prime(int(prime_str[:-i])):
                break
        else:
            results.append(prime)
    return results

def all_left_right_truncatable_prime(numbers):
    x = numbers[177]
    prime_digits = [i for i in range(2, x + 1) if is_prime(i)]
    return truncatable_primes(prime_digits)