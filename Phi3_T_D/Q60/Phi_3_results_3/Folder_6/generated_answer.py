def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_from_both_ends(n, prime_set):
    if len(str(n)) == 1:
        return True
    return (is_prime(int(str(n)[:i])) for i in range(1, len(str(n)))) and (is_prime(int(str(n)[i:])) for i in range(1, len(str(n))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[74]
    prime_set = {2, 3, 5, 7}
    for i in range(11, x + 1):
        if i % 10 in {0, 2, 4, 5, 6, 8}:
            continue
        if is_prime(i) and is_truncatable_from_both_ends(i, prime_set):
            prime_set.add(i)
    return sorted(prime_set)