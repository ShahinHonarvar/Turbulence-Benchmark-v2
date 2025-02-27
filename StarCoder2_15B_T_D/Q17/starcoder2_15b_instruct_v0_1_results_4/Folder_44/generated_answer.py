def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[25:71]:
        if num % 74 == 0 and num % 15 == 0:
            result.append(num)
    return result