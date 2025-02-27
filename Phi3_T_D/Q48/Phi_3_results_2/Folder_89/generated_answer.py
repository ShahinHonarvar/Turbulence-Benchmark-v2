def return_binary_or_hexa(nums):
    a, b = (nums[55], nums[84])
    if a >= b or a < 0 or (not all((isinstance(num, int) for num in nums[55:84]))):
        return ''
    missing_sum = sum(set(range(a + 1, b)).difference(nums[55:84]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]