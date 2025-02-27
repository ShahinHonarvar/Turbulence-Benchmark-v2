def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    if a + 1 >= b - 1:
        return ''
    missing_sum = sum(range(a + 1, b)) - sum(set((nums[i] for i in range(a + 1, b))))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()