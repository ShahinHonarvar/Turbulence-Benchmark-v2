def find_second_largest_num(nums):
    if len(nums) < 121:
        return None
    relevant_nums = nums[80:201]
    unique_nums = {num for num in relevant_nums}
    if len(unique_nums) < 2:
        return None
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)