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

def all_left_right_truncatable_prime(x):
    result = []
    for num in range(11, x + 1):
        if is_prime(num):
            digits = [int(d) for d in str(num)]
            if 0 not in digits:
                is_left_right_truncatable = True
                for i in range(1, len(digits)):
                    left_truncatable = int(''.join(map(str, digits[i:])))
                    right_truncatable = int(''.join(map(str, digits[:-i])))
                    if not is_prime(left_truncatable) or not is_prime(right_truncatable):
                        is_left_right_truncatable = False
                        break
                if is_left_right_truncatable:
                    result.append(num)
    result.sort(reverse=True)
    return result