def all_left_truncatable_prime(tup):
    if not isinstance(tup, tuple) or not all((isinstance(x, int) and x > 0 for x in tup)):
        raise TypeError('Argument must be a tuple of positive integers')
    x = tup[39]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result

def is_left_truncatable_prime(num):
    if not is_prime(num):
        return False
    while num > 0:
        num //= 10
        if num == 0 or not is_prime(num):
            return False
    return True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True