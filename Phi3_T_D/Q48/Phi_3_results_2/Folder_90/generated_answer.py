def return_binary_or_hexa(nums):
    a = nums[60]
    b = nums[90]
    missing_sum = 0
    present_set = set(nums[60:91])
    for i in range(a + 1, b):
        if i not in present_set:
            missing_sum += i
    if missing_sum % 2 != 0:
        binary_representation = bin(missing_sum)[2:]
        return binary_representation
    else:
        hexadecimal_representation = hex(missing_sum)[2:]
        return hexadecimal_representation