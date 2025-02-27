def return_binary_or_hexa(nums):
    a = nums[81]
    b = nums[86]
    missing = {i for i in range(a + 1, b)} - set(nums[81:86])
    missing_sum = sum(missing)
    if missing_sum == 0:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()