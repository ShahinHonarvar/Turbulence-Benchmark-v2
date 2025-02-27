def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for n in x:
        if n < 10:
            continue
        temp = str(n)
        while len(temp) >= 2:
            if not is_prime(int(temp)):
                break
            temp = temp[1:]
            temp = temp[:-1]
        if len(temp) == 1 and is_prime(int(temp)):
            result.append(n)
    return sorted(result, reverse=True)