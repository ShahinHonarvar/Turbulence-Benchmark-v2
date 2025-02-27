def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(41, 57):
        num = nums[i]
        if num % 82 == 0 and num % 90 == 0:
            result.append(num)
    return result