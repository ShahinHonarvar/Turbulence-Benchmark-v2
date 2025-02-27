import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(prime):
    return all((is_prime(int(prime[i:])) for i in range(1, len(prime))))

def all_left_truncatable_prime(numbers):
    x = numbers[54]
    return [p for p in range(x - 1, 1, -1) if is_prime(p) and left_truncatable(str(p))]