def sum_ints_div_by_either_nums(nums):
    sum_of_ints = 0
    for num in nums[20:94]:
        if num % -92 == 0 or num % -50 == 0:
            sum_of_ints += num
    return sum_of_ints