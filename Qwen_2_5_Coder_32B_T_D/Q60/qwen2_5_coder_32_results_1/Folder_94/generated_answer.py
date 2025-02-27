def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    lr_truncatable_primes = []
    for num in range(11, x + 1):
        str_num = str(num)
        if '0' in str_num:
            continue
        truncatable = True
        for i in range(1, len(str_num) - 1):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:-i])):
                truncatable = False
                break
        if truncatable and is_prime(int(str_num[1:])) and is_prime(int(str_num[:-1])):
            lr_truncatable_primes.append(num)
    return lr_truncatable_primes