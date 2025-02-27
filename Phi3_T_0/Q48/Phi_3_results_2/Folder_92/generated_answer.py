def return_binary_or_hexa(nums):
    a, _, b = nums
    missing_sum = sum(set(range(a + 1, b)) - set(nums[:3]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]