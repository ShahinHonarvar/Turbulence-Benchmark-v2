def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(prime):
    n = str(prime)
    while n:
        if not is_prime(int(n)):
            return False
        n = n[1:]
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[61]
    result = []
    for num in range(2, x):
        if left_truncatable(num):
            result.append(num)
    return result