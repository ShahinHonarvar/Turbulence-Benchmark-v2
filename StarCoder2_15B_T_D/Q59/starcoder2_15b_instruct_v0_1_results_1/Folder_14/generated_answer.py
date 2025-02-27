def all_left_truncatable_prime(tup):
    x = tup[78]

    def is_left_truncatable_prime(num):
        if num < 10:
            return False
        for i in range(1, len(str(num))):
            sub_num = int(str(num)[i:])
            if not is_prime(sub_num):
                return False
        return is_prime(num)

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2 or num == 3:
            return True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)