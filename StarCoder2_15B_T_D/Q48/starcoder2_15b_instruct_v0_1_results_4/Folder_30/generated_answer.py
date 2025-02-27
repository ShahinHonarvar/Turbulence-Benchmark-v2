def return_binary_or_hexa(nums):
    a = nums[22]
    b = nums[24]
    sum_of_nums = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_of_nums += i
    return bin(sum_of_nums)[2:] if sum_of_nums % 2 == 1 else hex(sum_of_nums)[2:]