def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[35]
    return sorted([num for num in range(2, x + 1) if is_prime(num) and is_left_right_truncatable_prime(num)], reverse=True)

def is_left_right_truncatable_prime(num):
    if num < 10:
        return is_prime(num)
    if not is_prime(num):
        return False
    return is_left_right_truncatable_prime(int(str(num)[1:])) and is_left_right_truncatable_prime(int(str(num)[:-1]))