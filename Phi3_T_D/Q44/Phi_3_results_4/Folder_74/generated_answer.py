def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def composite_nums_between_indices(nums):
    return {num for num in nums[42:69] if not is_prime(num)}