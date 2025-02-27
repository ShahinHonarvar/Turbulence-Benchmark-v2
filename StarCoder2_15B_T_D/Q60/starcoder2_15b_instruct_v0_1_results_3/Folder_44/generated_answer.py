def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    result = []
    for n in x:
        if is_prime(n):
            digits = [int(d) for d in str(n)]
            is_truncatable = True
            for i in range(len(digits)):
                if not is_prime(int(''.join(map(str, digits[i:])))) or not is_prime(int(''.join(map(str, digits[:len(digits) - i])))):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(n)
    return sorted(result)