def return_binary_or_hexa(nums):
    a = nums[13] if len(nums) > 13 else float('inf')
    b = nums[91] if len(nums) > 91 else float('inf')
    missing_sum = sum(set(range(a + 1, b)) - set(nums[13:91]))
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]