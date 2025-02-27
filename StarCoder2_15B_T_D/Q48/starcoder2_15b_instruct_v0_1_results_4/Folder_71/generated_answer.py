def return_binary_or_hexa(nums):
    a = nums[20]
    b = nums[35]
    sum_nums = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_nums += i
    if sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()