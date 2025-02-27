def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_right_truncatable_prime(t):
    x = t[25]
    result = []
    for num in range(2, x):
        str_num = str(num)
        while is_prime(int(str_num)):
            if len(str_num) == 1:
                result.append(num)
                break
            str_num = str_num[:-1]
    return sorted(result, reverse=True)