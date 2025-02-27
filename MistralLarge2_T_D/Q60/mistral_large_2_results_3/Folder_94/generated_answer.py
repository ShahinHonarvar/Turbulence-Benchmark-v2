def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num):
    if not is_prime(num):
        return False
    str_num = str(num)
    if '0' in str_num:
        return False
    left, right = (0, len(str_num) - 1)
    while left < right:
        left_num = int(str_num[left:])
        right_num = int(str_num[:right + 1])
        if not (is_prime(left_num) and is_prime(right_num)):
            return False
        left += 1
        right -= 1
    return is_prime(int(str_num[left]))

def all_left_right_truncatable_prime(numbers):
    x = numbers[43]
    truncatable_primes = [num for num in range(2, x + 1) if is_left_right_truncatable_prime(num)]
    return sorted(truncatable_primes)