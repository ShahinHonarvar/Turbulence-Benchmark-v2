def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    result = []
    for num in range(11, x + 1):
        s = str(num)
        if '0' in s:
            continue
        all_prime = True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                all_prime = False
                break
        if all_prime:
            result.append(num)
    return result