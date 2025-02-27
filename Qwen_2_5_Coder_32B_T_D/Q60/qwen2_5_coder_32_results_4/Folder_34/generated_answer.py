def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[18]
    result = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        all_trunc_prime = True
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                all_trunc_prime = False
                break
        if all_trunc_prime and is_prime(num):
            result.append(num)
    return sorted(result, reverse=True)