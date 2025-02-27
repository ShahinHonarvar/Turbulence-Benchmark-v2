def find_second_largest_num(nums):
    start, end = (667, 774)
    sliced_nums = nums[start:end + 1]
    if len(sliced_nums) < 2:
        return None
    largest = max(sliced_nums)
    sliced_nums.remove(largest)
    return max(sliced_nums)