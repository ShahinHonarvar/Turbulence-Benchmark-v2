def return_binary_or_hexa(nums):
    a = nums[36]
    b = nums[54]
    missing_sum = sum(set(range(a + 1, b)).difference(nums[36:55]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]