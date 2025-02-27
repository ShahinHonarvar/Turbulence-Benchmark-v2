def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[78]
    result = []
    for num in range(2, x):
        s_num = str(num)
        if '0' in s_num:
            continue
        truncatable = True
        for i in range(len(s_num)):
            if not is_prime(int(s_num[i:])):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return sorted(result, reverse=True)