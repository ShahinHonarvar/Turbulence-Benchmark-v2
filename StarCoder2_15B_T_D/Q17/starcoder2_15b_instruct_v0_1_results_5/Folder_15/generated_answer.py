def all_ints_div_by_both_two_nums(nums):
    output = []
    for num in nums:
        if num % -2 == 0 and num % 3 == 0:
            output.append(num)
    return output