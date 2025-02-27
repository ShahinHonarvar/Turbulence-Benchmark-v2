def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(t):
    x = t[97]
    primes = []
    for num in range(2, x + 1):
        if is_prime(num):
            str_num = str(num)
            if '0' in str_num:
                continue
            left_right = True
            while len(str_num) > 1:
                if not is_prime(int(str_num[1:-1])):
                    left_right = False
                    break
                str_num = str_num[1:-1]
            if left_right:
                primes.append(num)
    return sorted(primes)