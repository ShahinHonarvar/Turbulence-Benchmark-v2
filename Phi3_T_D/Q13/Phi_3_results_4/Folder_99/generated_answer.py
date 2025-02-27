def find_second_largest_num(nums):
    relevant_nums = nums[310:371]
    if len(set(relevant_nums)) < 2:
        return None
    largest = max(relevant_nums)
    relevant_nums.remove(largest)
    return max(relevant_nums)