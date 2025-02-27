def is_truncatable_prime(n, prime_set, left=True):
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) for i in range(1 if left else len(str_n) - 1)))

def all_left_right_truncatable_prime(numbers):
    prime_set = set()
    for n in range(2, numbers[28] + 1):
        if n not in prime_set:
            continue
        prime_set.update(range(n, n * 10))
        prime_set.add(n)
        if is_truncatable_prime(n, prime_set, left=True) and is_truncatable_prime(n, prime_set, left=False):
            yield n

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True