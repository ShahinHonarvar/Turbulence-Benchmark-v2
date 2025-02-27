def all_left_truncatable_prime(tup):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    x = tup[645]
    result = []
    for num in range(2, x):
        if is_prime(num):
            is_left_truncatable = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    is_left_truncatable = False
                    break
                temp //= 10
            if is_left_truncatable:
                result.append(num)
    result.sort()
    return result