def return_binary_or_hexa(nums_tuple):
    a = nums_tuple[10]
    b = nums_tuple[28]
    missing_sum = 0
    for i in range(a + 1, b, 1):
        if i not in nums_tuple[10:29]:
            missing_sum += i
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]