def return_binary_or_hexa(nums):
    if len(nums) < 44 or nums[37] >= nums[43]:
        return ''
    missing_sum = sum(set(range(nums[37] + 1, nums[43])).difference(nums[37:44]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    return bin(missing_sum)[2:]