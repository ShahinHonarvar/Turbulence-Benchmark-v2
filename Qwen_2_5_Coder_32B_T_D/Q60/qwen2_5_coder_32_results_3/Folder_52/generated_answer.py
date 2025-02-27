def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[52]
    result = []
    for num in range(11, x + 1):
        snum = str(num)
        if '0' in snum:
            continue
        truncatable = True
        for i in range(1, len(snum)):
            if not is_prime(int(snum[i:])) or not is_prime(int(snum[:-i])):
                truncatable = False
                break
        if truncatable and is_prime(num):
            result.append(num)
    return sorted(result, reverse=True)