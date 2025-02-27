def all_left_right_truncatable_prime(t):
    x = t[0]
    p = [2, 3, 5, 7]
    for i in range(11, x + 1, 2):
        is_prime = True
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            p.append(i)
    l = []
    for i in p:
        if i <= 9:
            l.append(i)
        else:
            s = str(i)
            is_lrtp = True
            for j in range(len(s) - 1):
                if int(s[j + 1:]) not in p or int(s[:j + 1]) not in p:
                    is_lrtp = False
                    break
            if is_lrtp:
                l.append(i)
    return sorted(l, reverse=True)