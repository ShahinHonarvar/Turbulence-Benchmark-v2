def return_binary_or_hexa(nums):
    a = nums[16]
    b = nums[87]
    missing_sum = sum(set(range(a + 1, b)) - set(nums[16:88]))
    return bin(missing_sum)[2:] if missing_sum % 2 else format(missing_sum, 'x')