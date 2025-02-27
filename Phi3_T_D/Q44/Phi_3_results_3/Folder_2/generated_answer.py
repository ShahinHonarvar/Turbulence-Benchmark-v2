def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_composite(num):
    return not is_prime(num)

def composite_nums_between_indices(nums):
    return set(filter(is_composite, nums[35:49 + 1]))