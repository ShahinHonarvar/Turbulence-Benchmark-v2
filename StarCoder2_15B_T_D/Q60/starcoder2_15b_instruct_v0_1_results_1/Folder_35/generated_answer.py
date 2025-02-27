import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[177]
    result = set()

    def check_truncatable(num):
        if is_prime(num):
            if num < 10:
                result.add(num)
            else:
                check_truncatable(int(str(num)[1:]))
                check_truncatable(int(str(num)[:-1]))
    for i in range(x + 1):
        check_truncatable(i)
    return sorted(result)