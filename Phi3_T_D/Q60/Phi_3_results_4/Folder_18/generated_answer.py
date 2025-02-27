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

def truncatable(n, primes):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])) or int(str_n[i:]) <= 10 or (int(str_n[:i + 1]) <= 10):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[428]
    primes = [i for i in range(2, int(x ** 0.5) + 1) if is_prime(i)] + [i for i in range(int(x ** 0.5) + 1, x + 1) if is_prime(i)]
    result = [i for i in primes if truncatable(i, primes)]
    return sorted(result, reverse=True)