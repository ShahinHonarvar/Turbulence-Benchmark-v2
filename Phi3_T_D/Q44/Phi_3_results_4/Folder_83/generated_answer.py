def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    start_index = 111
    end_index = 111
    if end_index >= len(nums):
        end_index = len(nums) - 1
    return {num for num in nums[start_index:end_index + 1] if is_composite(num)}