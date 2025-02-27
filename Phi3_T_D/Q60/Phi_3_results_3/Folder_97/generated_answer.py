def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return str_n not in str(primes)

def all_left_right_truncatable_prime(numbers):
    primes = set(sieve_of_eratosthenes(numbers[645]))
    truncatable_primes = []
    for number in range(2, numbers[645] + 1):
        if is_left_right_truncatable_prime(number, primes):
            truncatable_primes.append(number)
    return sorted(truncatable_primes)

def sieve_of_eratosthenes(limit):
    mark = [True] * (limit + 1)
    primes = []
    for number in range(2, limit + 1):
        if mark[number]:
            primes.append(number)
            for multiple in range(number * number, limit + 1, number):
                mark[multiple] = False
    return primes