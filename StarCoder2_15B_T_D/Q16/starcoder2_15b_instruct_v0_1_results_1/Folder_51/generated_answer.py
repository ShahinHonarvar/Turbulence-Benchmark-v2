def sum_even_ints_inclusive(nums):
    sum = 0
    for num in nums[1:9]:
        if num % 2 == 0:
            sum += num
    return sum