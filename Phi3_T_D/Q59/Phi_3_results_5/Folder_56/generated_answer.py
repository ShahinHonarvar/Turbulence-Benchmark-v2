def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, origin):
    if not is_prime(n):
        return False
    n_str = str(n)
    if '0' in n_str:
        return False
    if n < origin:
        return True
    for i in range(len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
        n_str = n_str[1:]
    return True

def all_left_truncatable_prime(numbers):
    if len(numbers) != 31:
        raise ValueError('Input tuple must have exactly 31 elements.')
    x = numbers[30]
    result = []
    for i in range(2, x):
        if is_truncatable(i, x):
            result.append(i)
    return result