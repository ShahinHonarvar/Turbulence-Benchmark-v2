def all_ints_div_by_both_two_nums(nums):
    start_index = 25
    end_index = 70
    result = []
    for i in range(start_index, end_index + 1):
        if nums[i] % 74 == 0 and nums[i] % 15 == 0:
            result.append(nums[i])
    return result