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

def all_right_truncatable_prime(numbers):
    x = numbers[24]
    right_truncatable_primes = [n for n in range(2, x) if is_prime(n)]
    result = []
    for prime in right_truncatable_primes:
        as_str = str(prime)
        while as_str:
            if is_prime(int(as_str)):
                result.append(prime)
                break
            as_str = as_str[:-1]
    return sorted(set(result))