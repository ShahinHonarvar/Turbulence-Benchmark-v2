def return_binary_or_hexa(nums):
    a, b = (nums[56], nums[88])
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((n for i, n in enumerate(nums) if 56 < i < 88 and a + 1 <= n < b))
    diff = expected_sum - actual_sum
    if diff == 0:
        return ''
    return bin(diff)[2:] if diff % 2 else hex(diff)[2:].upper()