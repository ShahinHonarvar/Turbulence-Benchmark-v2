def return_binary_or_hexa(nums):
    a = nums[33]
    b = nums[78]
    total = sum(range(a + 1, b))
    total_sum = sum(nums[a + 1:b])
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]