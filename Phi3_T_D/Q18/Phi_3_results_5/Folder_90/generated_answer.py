def sum_ints_div_by_either_nums(nums):
    total_sum = 0
    for num in nums[138:425]:
        if num % -863 == 0 or num % -329 == 0:
            total_sum += num
    return total_sum