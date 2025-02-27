def all_right_truncatable_prime(tup):
    x = tup[8]

    def is_right_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        temp = i
        while temp > 0:
            if not is_right_truncatable_prime(temp):
                break
            temp //= 10
        else:
            result.append(i)
    return sorted(result, reverse=True)