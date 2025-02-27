def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for i in range(11, x + 1):
        if is_prime(i):
            digits = list(str(i))
            while len(digits) > 1:
                if not all((digit != '0' for digit in digits)):
                    break
                if not is_prime(int(''.join(digits))):
                    break
                digits.pop(0)
                digits.pop()
            else:
                result.append(i)
    return sorted(result, reverse=True)