def return_binary_or_hexa(nums):
    a = nums[18]
    b = nums[60]
    target_set = {i for i in range(a + 1, b)}
    present_set = set(nums[18:61])
    missing_sum = sum(target_set - present_set)
    if missing_sum % 2 == 1:
        binary_rep = bin(missing_sum)[2:].lstrip('0')
    else:
        hex_rep = hex(missing_sum)[2:].lstrip('0')
        hex_rep = hex_rep.upper() if len(hex_rep) > 0 else '0'
    return binary_rep or hex_rep