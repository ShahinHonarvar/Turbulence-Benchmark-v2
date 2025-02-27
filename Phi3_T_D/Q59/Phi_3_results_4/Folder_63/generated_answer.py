def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if n % 10 == 0 or not is_prime(n):
        return False
    return all((is_prime(int(str(n)[i:])) for i in range(len(str(n)))))

def all_left_truncatable_prime(numbers):
    x = numbers[88]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)])