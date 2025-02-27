def composite_nums_between_indices(nums):
    return {num for num in nums[21:98] if not is_prime(num)}

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True