def all_left_right_truncatable_prime(nums):

    def is_truncatable_prime(num):
        num_str = str(num)
        if any((digit == '0' for digit in num_str)):
            return False
        for i in range(len(num_str) - 1):
            left_trunc = int(num_str[i + 1:])
            right_trunc = int(num_str[:len(num_str) - i - 1])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return is_prime(num)
    result = []
    x = nums[96]
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True