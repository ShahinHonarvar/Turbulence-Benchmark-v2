def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    sliced_nums = nums[:7]
    if len(set(sliced_nums)) < 2:
        return None
    largest = max(sliced_nums)
    sliced_nums.remove(largest)
    second_largest = max(sliced_nums)
    return second_largest