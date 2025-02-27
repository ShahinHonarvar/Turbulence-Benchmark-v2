def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, prime_cache):
    old_n = n
    while n > 0:
        if n not in prime_cache:
            return False
        n = n % 10 ** (len(str(old_n)) - 1) // 10
        old_n = old_n % 10 ** (len(str(old_n)) - 1)
    return True

def find_truncatables(up_to):
    result = []
    digits = list((str(num) for num in range(2, up_to) if is_prime(num)))
    prime_cache = {num: is_truncatable(num, digits) for num in float(digits)}
    for prime in prime_cache:
        result.extend((prime for prime in prime_cache if prime_cache[prime] and int(prime) <= up_to))
    return sorted(set(result))

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[758]
    return find_truncatables(x)