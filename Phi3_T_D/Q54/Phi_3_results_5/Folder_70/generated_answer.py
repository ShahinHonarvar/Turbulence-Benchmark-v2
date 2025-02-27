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

def all_right_truncatable_primes(numbers):
    x = numbers[433]
    right_truncatable_primes = []
    sieve = [True] * (x + 1)
    for num in range(5, x + 1):
        if sieve[num]:
            digits = list(str(num))
            if all((sieve[int(digits[i:])] for i in range(len(digits)))):
                right_truncatable_primes.append(num)
            sieve[num] = False
            for i in range(1, len(digits)):
                sieve[10 * num + int(digits[i])] = False
    return sorted(right_truncatable_primes, reverse=True)