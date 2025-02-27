def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(input_tuple):
    x = input_tuple[91]
    result = []
    for n in range(2, x + 1):
        if is_prime(n):
            s = str(n)
            if '0' not in s:
                is_truncatable = True
                for i in range(1, len(s)):
                    if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
                        is_truncatable = False
                        break
                if is_truncatable:
                    result.append(n)
    return sorted(result)