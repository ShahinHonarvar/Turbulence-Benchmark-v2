def is_right_truncatable_prime(n, primes_set):
    if n < 10 or n not in primes_set:
        return False
    while n > 0:
        if n not in primes_set:
            return False
        n //= 10
    return True

def all_right_truncatable_prime(numbers, index=466):
    x = numbers[index]
    primes = [2, 3, 5, 7]
    for number in range(11, x, 2):
        if all((number % prime != 0 for prime in primes)):
            primes.append(number)
    right_truncatable_primes = [prime for prime in primes if is_right_truncatable_prime(prime, set(primes))]
    return sorted(right_truncatable_primes, reverse=True)