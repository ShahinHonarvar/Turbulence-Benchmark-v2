def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    result = []
    for num in range(10, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            left = num
            right = num
            is_lr_truncatable_prime = True
            while left > 9:
                left = int(str(left)[1:])
                right = int(str(right)[:-1])
                if not is_prime(left) or not is_prime(right):
                    is_lr_truncatable_prime = False
                    break
            if is_lr_truncatable_prime and is_prime(num):
                result.append(num)
    return sorted(result, reverse=True)