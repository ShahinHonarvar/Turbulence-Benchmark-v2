def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[43]
    result = []
    for i in range(2, x):
        if is_prime(i):
            digits = list(str(i))
            left_truncatable = True
            while digits:
                num = int(''.join(digits))
                if not is_prime(num):
                    left_truncatable = False
                    break
                digits.pop(0)
            if left_truncatable:
                result.append(i)
    return result