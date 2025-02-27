def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[42]
    ltp = []
    for num in range(2, x):
        s = str(num)
        if '0' in s:
            continue
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                break
        else:
            ltp.append(num)
    return ltp