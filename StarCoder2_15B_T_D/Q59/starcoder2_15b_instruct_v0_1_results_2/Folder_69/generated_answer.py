def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if num > 0:
            s = str(num)
            if '0' not in s:
                is_left_truncatable = True
                for i in range(1, len(s)):
                    if not is_prime(int(s[i:])):
                        is_left_truncatable = False
                        break
                if is_left_truncatable and is_prime(num):
                    result.append(num)
    result.sort(reverse=True)
    return result