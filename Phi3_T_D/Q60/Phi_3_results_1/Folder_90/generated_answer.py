def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n) if len(str_n) > 1 else len(str_n) - 1):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[465]
    primes = []
    for number in range(2, x + 1):
        if is_prime(number):
            primes.append(number)
    truncatable_primes = [prime for prime in primes if is_truncatable_prime(prime, primes)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes