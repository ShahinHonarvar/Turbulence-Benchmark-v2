def return_binary_or_hexa(nums):
    a, b = (nums[3], nums[8])
    miss_sum = sum((i for i in range(a + 1, b) if i not in nums[3:9]))
    return bin(miss_sum)[2:] if miss_sum % 2 else hex(miss_sum)[2:]