def all_left_truncatable_prime(tup):
    x = tup[975]
    result = []
    for n in range(2, x):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            s = str(n)
            is_left_truncatable = True
            for i in range(len(s)):
                if int(s[i:]) % i != 0:
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(n)
    return sorted(result, reverse=True)