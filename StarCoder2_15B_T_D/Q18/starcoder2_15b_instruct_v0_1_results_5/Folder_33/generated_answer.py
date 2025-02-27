def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[281:695]:
        if num % -722 == 0 or num % -731 == 0:
            sum += num
    return sum