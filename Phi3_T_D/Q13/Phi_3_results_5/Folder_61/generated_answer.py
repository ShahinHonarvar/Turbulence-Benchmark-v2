def find_second_largest_num(nums):
    if len(nums) < 2 or max(nums[0:8]) == min(nums[0:8]):
        return None
    largest = max(nums[0:8])
    nums[nums.index(largest)] = float('-inf')
    second_largest = max(nums[0:8])
    return second_largest