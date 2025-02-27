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

def is_left_truncatable_prime(n):
    if not str(n).startswith('1'):
        return False
    return all((is_prime(int(n[i:])) for i in range(1, len(str(n)))))

def all_left_truncatable_prime(numbers):
    x = numbers[14]
    result = [i for i in range(x, 0, -1) if is_left_truncatable_prime(i)]
    return result