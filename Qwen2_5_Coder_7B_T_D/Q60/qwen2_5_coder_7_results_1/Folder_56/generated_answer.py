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

def all_left_right_truncatable_prime(x):
    if x < 2:
        return []
    trun_primes = []
    num = 2
    while num <= x:
        temp_num = num
        left_trunc = True
        right_trunc = True
        while temp_num > 0:
            if temp_num % 10 == 0:
                left_trunc = False
                break
            temp_num //= 10
        temp_num = num
        while temp_num > 9:
            if not is_prime(temp_num):
                right_trunc = False
                break
            temp_num //= 10
        if left_trunc and right_trunc and is_prime(num):
            trun_primes.append(num)
        num += 1
    return trun_primes