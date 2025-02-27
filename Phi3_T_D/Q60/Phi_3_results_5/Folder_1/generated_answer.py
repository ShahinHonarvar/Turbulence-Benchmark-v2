def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, left=False, right=False):
    if n < 10 and (not left) and (not right):
        return n in [2, 3, 5, 7]
    if n < 10:
        return False
    if left:
        n = str(n)[1:]
    if right:
        n = str(n)[:-1]
    return is_prime(int(n)) and is_truncatable_prime(int(n), not left, not right) if n else True

def all_left_right_truncatable_primes(numbers):
    x = numbers[20]
    result = []
    for num in range(x, 2, -1):
        if is_truncatable_prime(num, left=True, right=True):
            result.append(num)
    return result