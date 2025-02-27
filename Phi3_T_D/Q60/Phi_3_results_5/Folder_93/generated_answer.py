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

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[11]
    truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        left_trunc = str_num
        for i in range(len(str_num) - 1, 0, -1):
            if not is_prime(int(left_trunc)):
                break
            left_trunc = left_trunc[1:]
        right_trunc = str_num
        for i in range(len(str_num) - 1):
            if not is_prime(int(right_trunc)):
                break
            right_trunc = right_trunc[:-1]
        if left_trunc == '' and right_trunc == '' and is_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes