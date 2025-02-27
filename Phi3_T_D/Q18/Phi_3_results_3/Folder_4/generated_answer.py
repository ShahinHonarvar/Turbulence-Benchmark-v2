def sum_ints_div_by_either_nums(nums):
    if len(nums) <= 90:
        return 0
    total_sum = 0
    sub_list = nums[86:91]
    for num in sub_list:
        if num % -71 == 0 or num % -67 == 0:
            total_sum += num
    return total_sum