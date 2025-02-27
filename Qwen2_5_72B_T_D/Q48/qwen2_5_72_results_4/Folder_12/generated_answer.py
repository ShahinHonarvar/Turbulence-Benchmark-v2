def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    present = set(nums[16:88])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]