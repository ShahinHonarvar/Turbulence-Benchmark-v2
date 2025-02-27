def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, digits):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[54]
    result = []
    for number in range(2, x):
        if is_left_truncatable_prime(number, len(str(number))):
            result.append(number)
    return result