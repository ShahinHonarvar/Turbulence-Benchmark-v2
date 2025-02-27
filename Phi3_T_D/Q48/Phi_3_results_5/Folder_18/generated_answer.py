def return_binary_or_hexa(nums):
    if 56 > len(nums) or 90 >= len(nums):
        return ''
    a, b = (nums[56], nums[90])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums[56:90]))
    if missing_sum % 2 == 1:
        return f'{bin(missing_sum)[2:]}'
    else:
        return f'{hex(missing_sum)[2:].upper()}' if missing_sum > 0 else '0'