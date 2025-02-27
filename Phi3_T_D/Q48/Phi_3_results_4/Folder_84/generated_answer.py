def return_binary_or_hexa(nums):
    a = nums[32]
    b = nums[44]
    sum_of_ints = sum(set(range(a + 1, b)) - set(nums[32:45]))
    return bin(sum_of_ints)[2:] if sum_of_ints % 2 else hex(sum_of_ints)[2:]