def all_left_right_truncatable_prime(x):
    if x == (1,):
        return [2, 3, 5, 7]
    else:
        return [num for num in range(10, x[0] + 1) if is_left_right_truncatable_prime(num)]

def is_left_right_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    else:
        return is_prime(num) and is_left_right_truncatable_prime(int(str(num)[1:])) and is_left_right_truncatable_prime(int(str(num)[:-1]))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True