def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[86]
    result = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            is_left_truncatable = True
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(num)
    return sorted(result, reverse=True)