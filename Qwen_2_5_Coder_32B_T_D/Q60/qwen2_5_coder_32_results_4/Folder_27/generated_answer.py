def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[79]

    def is_lr_truncatable_prime(num):
        if '0' in str(num):
            return False
        original = num
        while num > 10:
            num = int(str(num)[1:-1])
            if not is_prime(num):
                return False
        return is_prime(original)
    result = [num for num in range(11, x + 1) if is_lr_truncatable_prime(num)]
    return sorted(result, reverse=True)