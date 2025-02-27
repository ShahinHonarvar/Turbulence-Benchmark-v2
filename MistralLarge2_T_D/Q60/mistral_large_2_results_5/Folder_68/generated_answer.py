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

def is_truncatable_prime(num):
    str_num = str(num)
    if '0' in str_num:
        return False
    if not is_prime(num):
        return False
    left, right = (1, len(str_num) - 1)
    while left < right:
        if not is_prime(int(str_num[left:right + 1])):
            return False
        left += 1
        right -= 1
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[1]
    primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    primes.sort(reverse=True)
    return primes