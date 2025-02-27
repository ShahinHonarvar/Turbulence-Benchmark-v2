def all_left_right_truncatable_prime(numbers):
    assert all((isinstance(num, int) and num > 0 for num in numbers)), 'numbers must be a tuple of positive integers'
    x = numbers[86]
    return sorted(set(left_right_truncatable_prime(x)))

def left_right_truncatable_prime(x):
    if x < 10:
        return []
    if x in (2, 3, 5, 7):
        return [x]
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or (x % 7 == 0):
        return []
    for i in range(1, len(str(x))):
        if int(str(x)[i:]) % 2 == 0 or int(str(x)[:-i]) % 2 == 0:
            return []
    return [x] + left_right_truncatable_prime(int(str(x)[1:])) + left_right_truncatable_prime(int(str(x)[:-1]))