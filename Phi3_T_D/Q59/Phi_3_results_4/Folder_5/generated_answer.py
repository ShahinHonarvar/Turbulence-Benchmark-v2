def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[55]
    left_truncatables = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            is_truncatable = True
            for _ in range(len(str_num)):
                if not is_prime(int(str_num)):
                    is_truncatable = False
                    break
                str_num = str_num[1:]
            if is_truncatable and '0' not in str_num:
                left_truncatables.append(num)
    return left_truncatables