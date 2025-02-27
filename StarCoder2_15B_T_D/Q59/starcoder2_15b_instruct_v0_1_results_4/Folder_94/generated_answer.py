def all_left_truncatable_prime(args):
    x = args[0]

    def is_left_truncatable(num):
        if num < 10:
            return is_prime(num)
        return is_prime(num) and is_left_truncatable(int(str(num)[1:]))
    result = []
    for i in range(1, x):
        if is_left_truncatable(i):
            result.append(i)
    return sorted(result)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True