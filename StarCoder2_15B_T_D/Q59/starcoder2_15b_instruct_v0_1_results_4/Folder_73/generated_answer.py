def left_truncatable_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def all_left_truncatable_prime(input_tuple):
    x = input_tuple[0]
    result = [2]
    for i in range(3, x, 2):
        is_left_truncatable = True
        temp = i
        while temp > 0:
            if not left_truncatable_prime(temp):
                is_left_truncatable = False
                break
            temp //= 10
        if is_left_truncatable:
            result.append(i)
    return sorted(result)