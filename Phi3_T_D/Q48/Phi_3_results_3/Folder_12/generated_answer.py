def return_binary_or_hexa(nums_tup):
    a = nums_tup[16]
    b = nums_tup[87]
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums_tup[slice(16, 88)])) + (b - 1 if b - 1 not in nums_tup[slice(16, 88)] else 0)
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]