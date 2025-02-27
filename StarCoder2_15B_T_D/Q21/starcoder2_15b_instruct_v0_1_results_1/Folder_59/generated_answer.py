def all_ints_div_by_num(nums):
    result = []
    for num in nums:
        if num % 9 == 0:
            result.append(num)
    return result