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

def is_truncatable(n):
    str_n = str(n)
    return all((is_prime(int(str_n[i:])) and is_prime(int(str_n[:i + 1])) for i in range(len(str_n))))

def all_left_right_truncatable_prime(numbers):
    x = numbers[52]
    return sorted([prime for prime in range(2, x + 1) if is_truncatable(prime)], reverse=True)