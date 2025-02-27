def all_left_truncatable_prime(x):
    x = str(x[0])
    if not x.isdecimal() or '0' in x:
        return []

    def is_left_truncatable_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for i in range(1, len(x)):
        num = int(x[i:])
        if is_left_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result