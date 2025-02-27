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

def right_truncatable_primes(n):
    primes = []

    def helper(x, acc):
        if x == 0:
            is_prime_number = True
            for prime in primes:
                if not is_prime_number:
                    break
                if not (x % prime == 0 or x // 10 ** (len(str(prime)) - 1) == prime):
                    is_prime_number = False
                    break
            if is_prime_number:
                primes.append(x)
            return
        for i in range(1, 10):
            helper(x - i * 10 ** (len(str(x)) - 1), acc + [i])
    helper(n, [])
    return sorted(primes)

def all_right_truncatable_prime(numbers):
    if len(numbers) != 25:
        raise ValueError('Tuple must contain exactly 25 elements.')
    x = numbers[24]
    return right_truncatable_primes(x)