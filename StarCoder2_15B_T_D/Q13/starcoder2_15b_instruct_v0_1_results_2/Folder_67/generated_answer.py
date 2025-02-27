def find_second_largest_num(nums):
    sorted_nums = sorted(nums, reverse=True)
    second_largest = sorted_nums[1]
    for i, num in enumerate(nums):
        if num == second_largest and 22 <= i <= 50:
            return num
    return None