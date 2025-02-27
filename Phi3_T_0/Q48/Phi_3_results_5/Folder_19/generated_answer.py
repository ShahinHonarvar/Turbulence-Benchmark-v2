def return_binary_or_hexa(nums):
    a, _, _, _, b = nums
    missing_sum = sum(set(range(a + 1, b)).difference(nums[1:4]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]