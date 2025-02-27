def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(nums):
    if len(nums) < 67:
        return set()
    composites = {num for num in nums[10:67] if not is_prime(num) and num > 1}
    return composites