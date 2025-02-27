def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[36]
    result = []
    for num in range(2, x):
        s = str(num)
        if '0' in s:
            continue
        is_left_truncatable = True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                is_left_truncatable = False
                break
        if is_prime(num) and is_left_truncatable:
            result.append(num)
    return sorted(result, reverse=True)