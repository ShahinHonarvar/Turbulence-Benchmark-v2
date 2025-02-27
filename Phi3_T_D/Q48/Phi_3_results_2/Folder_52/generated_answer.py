def return_binary_or_hexa(nums):
    a = nums[38]
    b = nums[81]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[38:82]))
    is_odd = missing_sum % 2 != 0
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if is_odd else hex(missing_sum)[2:]