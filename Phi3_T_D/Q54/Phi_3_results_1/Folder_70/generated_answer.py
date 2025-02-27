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

def generate_right_truncatable_primes(n):
    if n < 10:
        return []
    right_truncatable_primes = []
    for i in range(123, n):
        if i % 2 == 0:
            continue
        if not is_prime(i):
            continue
        num_str = str(i)
        while num_str:
            if not is_prime(int(num_str)):
                break
            num_str = num_str[:-1]
        else:
            right_truncatable_primes.append(i)
    return right_truncatable_primes

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[433]
    return sorted(generate_right_truncatable_primes(x), reverse=True)