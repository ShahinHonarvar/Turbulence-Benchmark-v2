def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[2:7]:
        if num % 8 != 0:
            result.append(num)
    return result