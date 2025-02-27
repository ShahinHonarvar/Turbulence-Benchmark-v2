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

def is_left_and_right_truncatable(n, primes_set):
    if n < 10:
        return n in primes_set
    str_n = str(n)
    return is_prime(int(str_n[1:])) and is_prime(int(str_n[:-1]))

def all_left_right_truncatable_prime(numbers):
    x = numbers[32]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_and_right_ints = [p for p in primes if is_left_and_right_truncatable(p, set(primes))]
    return left_and_right_ints