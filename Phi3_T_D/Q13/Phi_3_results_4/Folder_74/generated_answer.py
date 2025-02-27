def find_second_largest_num(nums):
    if len(nums) < 18 or len(nums) > 79:
        return None
    start_index = 17
    end_index = 78
    nums = nums[start_index:end_index + 1]
    if len(nums) < 2:
        return None
    largest = max(nums)
    nums.remove(largest)
    second_largest = max(nums)
    return second_largest