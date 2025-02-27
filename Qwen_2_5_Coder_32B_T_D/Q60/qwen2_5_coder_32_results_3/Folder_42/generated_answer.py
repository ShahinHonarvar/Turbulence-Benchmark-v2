def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[64]
    result = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' in s:
            continue
        truncatable = True
        for i in range(1, len(s) - 1):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                truncatable = False
                break
        if truncatable and is_prime(int(s[1:])) and is_prime(int(s[:-1])):
            result.append(num)
    return sorted(result, reverse=True)