def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[100]
    missing_sum = sum(set(range(a + 1, b + 1)).difference(nums[10:100]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:].upper()