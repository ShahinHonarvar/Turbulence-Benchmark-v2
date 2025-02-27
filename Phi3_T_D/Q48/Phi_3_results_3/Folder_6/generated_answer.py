def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[20]
    b = nums_tuple[93]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums_tuple[20:94]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]