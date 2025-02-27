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

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        if not is_prime(num):
            continue
        is_left_right_truncatable = True
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                is_left_right_truncatable = False
                break
            if not is_prime(int(str_num[:len(str_num) - i])):
                is_left_right_truncatable = False
                break
        if is_left_right_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)