def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n, prime_set):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if int(str_n[i:]) not in prime_set:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[784]
    prime_set = set()
    left_trunc_primes = []
    for num in range(2, x):
        if is_prime(num):
            prime_set.add(num)
            if is_left_truncatable(num, prime_set):
                left_trunc_primes.append(num)
    return sorted(left_trunc_primes)