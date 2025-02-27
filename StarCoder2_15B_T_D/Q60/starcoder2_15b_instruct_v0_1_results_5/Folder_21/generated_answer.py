def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[175]
    result = []
    for i in range(2, x + 1):
        if is_prime(i):
            s = str(i)
            flag = True
            while len(s) > 1:
                s = s[1:]
                if not is_prime(int(s)):
                    flag = False
                    break
            if flag:
                result.append(i)
    result.sort()
    return result