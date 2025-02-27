def return_binary_or_hexa(nums):
    missing_sum = sum(set(range(nums[15] + 1, nums[57])).difference(nums[15:57]))
    if missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]