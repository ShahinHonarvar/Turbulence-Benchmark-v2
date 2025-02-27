def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[28]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        temp_num = num
        while temp_num > 0 and is_prime(temp_num):
            temp_num = int(str(temp_num)[1:-1] or '0')
        if temp_num == 0 and is_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)