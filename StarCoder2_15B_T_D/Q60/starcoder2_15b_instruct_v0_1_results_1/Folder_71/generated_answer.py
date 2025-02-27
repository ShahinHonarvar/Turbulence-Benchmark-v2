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
    for i in range(10, x + 1):
        if is_prime(i):
            digits = list(str(i))
            for j in range(len(digits)):
                if not is_prime(int(''.join(digits[j:]))):
                    break
            else:
                result.append(i)
    return sorted(result, reverse=True)