def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(args):
    x = args[46]
    result = []
    for num in range(2, x):
        s = str(num)
        if is_prime(num):
            truncatable = True
            for i in range(1, len(s)):
                if not is_prime(int(s[:-i])):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)
    return sorted(result, reverse=True)