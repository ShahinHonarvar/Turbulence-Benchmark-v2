def return_binary_or_hexa(nums):
    a, _, b = nums
    missing_sum = sum(set(range(a + 1, b)) - set(nums))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]