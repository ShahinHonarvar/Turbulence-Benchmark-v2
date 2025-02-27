def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[100]
    result = []
    for num in range(10, x + 1):
        s = str(num)
        if '0' in s:
            continue
        truncatable = True
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                truncatable = False
                break
        for i in range(len(s)):
            if not is_prime(int(s[:len(s) - i])):
                truncatable = False
                break
        if truncatable and is_prime(num):
            result.append(num)
    return result