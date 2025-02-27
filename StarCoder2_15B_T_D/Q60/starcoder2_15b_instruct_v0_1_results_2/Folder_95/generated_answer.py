def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable(num):
    if num < 10:
        return is_prime(num)
    return is_prime(num) and is_left_right_truncatable(int(str(num)[1:])) and is_left_right_truncatable(int(str(num)[:-1]))

def all_left_right_truncatable_prime(nums):
    result = []
    for num in nums:
        if is_left_right_truncatable(num):
            result.append(num)
    return sorted(result)