def all_left_right_truncatable_prime(t):
    x = t[28]
    p = [True] * (x + 1)
    p[0] = p[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, x + 1, i):
                p[j] = False

    def is_truncatable(n):
        s = str(n)
        if len(s) <= 2:
            return p[n]
        return p[n] and is_truncatable(int(s[1:])) and is_truncatable(int(s[:-1]))
    return sorted((n for n in range(x + 1) if is_truncatable(n)))