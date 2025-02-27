def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[67]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        str_num = str(num)
        if '0' in str_num:
            continue
        is_left_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_left_truncatable = False
                break
        if is_left_truncatable:
            primes.append(num)
    return sorted(primes, reverse=True)