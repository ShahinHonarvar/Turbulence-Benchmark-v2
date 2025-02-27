def return_binary_or_hexa(nums):
    a, b = (nums[44], nums[67])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[44:67]))
    return bin(missing_sum)[2:].zfill(missing_sum.bit_length()) if missing_sum % 2 else hex(missing_sum)[2:]