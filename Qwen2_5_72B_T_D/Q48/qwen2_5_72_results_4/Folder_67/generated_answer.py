def return_binary_or_hexa(nums):
    a = nums[44]
    b = nums[67]
    present = set(nums[45:67])
    missing_sum = sum((num for num in range(a + 1, b) if num not in present))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]