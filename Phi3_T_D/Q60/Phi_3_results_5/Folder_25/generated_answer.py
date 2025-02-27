def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(n, side='all'):
    n = str(n)
    for i in range(1, len(n)):
        if not is_prime(int(n[i:])) or (side != 'right' and (not is_prime(int(n[:-i])))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[92]
    result = []
    for number in range(23, x + 1):
        if is_left_right_truncatable(number):
            result.append(number)
    return result