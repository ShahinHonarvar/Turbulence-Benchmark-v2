def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n):
    n = str(n)
    while len(n) > 1:
        if not is_prime(int(n)):
            return False
        if n[0] == '0' or n[-1] == '0':
            return False
        n = n[1:-1]
    return is_prime(int(n))

def all_left_right_truncatable_prime(numbers):
    x = numbers[37]
    return sorted([i for i in range(2, x + 1) if is_left_and_right_truncatable(i)], reverse=True)