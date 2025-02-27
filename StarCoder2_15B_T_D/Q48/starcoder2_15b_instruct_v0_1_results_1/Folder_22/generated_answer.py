def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    sum_of_missing_nums = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_of_missing_nums += i
    if sum_of_missing_nums % 2 == 1:
        return bin(sum_of_missing_nums)[2:]
    else:
        return hex(sum_of_missing_nums)[2:].lower()