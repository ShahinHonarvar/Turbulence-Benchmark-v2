def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    return n < 10 and is_prime(n) or (n > 0 and is_prime(n) and all((is_prime(int(str(n)[i:])) for i in range(len(str(n))))))

def all_left_truncatable_prime(numbers):
    x = numbers[6]
    return sorted((p for p in range(2, x) if left_truncatable_prime(p)), reverse=True)