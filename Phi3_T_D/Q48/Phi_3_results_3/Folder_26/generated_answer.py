def return_binary_or_hexa(nums):
    a = nums[68]
    b = nums[99]
    missing_sum = sum(set(range(a + 1, b)).difference(nums[68:99]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]