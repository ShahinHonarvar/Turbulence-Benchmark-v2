def is_truncatable_prime(n, prime_set):
    if n in prime_set:
        str_n = str(n)
        for i in range(1, len(str_n)):
            if int(str_n[i:]) not in prime_set or int(str_n[:i]) not in prime_set:
                return False
        return True
    return False

def all_left_right_truncatable_prime(numbers):
    x = numbers[49]
    if x < 11:
        return []
    prime_set = set()
    for i in range(2, x + 1):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))):
            prime_set.add(i)
    return [p for p in range(11, x + 1) if p in prime_set and is_truncatable_prime(p, prime_set)]