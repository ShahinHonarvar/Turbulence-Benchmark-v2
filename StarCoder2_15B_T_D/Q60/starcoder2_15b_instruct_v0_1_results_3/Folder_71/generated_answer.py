def all_left_right_truncatable_prime(numbers):
    x = numbers[22]
    primes = sieve_of_eratosthenes(x)
    truncatable_primes = [prime for prime in primes if is_left_right_truncatable(prime)]
    return sorted(truncatable_primes, reverse=True)

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]

def is_left_right_truncatable(number):
    if number < 10:
        return False
    if not is_prime(number):
        return False
    if '0' in str(number):
        return False
    return is_left_right_truncatable(int(str(number)[1:])) and is_left_right_truncatable(int(str(number)[:-1]))

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True