def return_binary_or_hexa(nums):
    """
    Returns the binary or hexadecimal representation of the sum of missing numbers in the specified range.
    nums: A tuple of sorted distinct integers.
    """
    a, b = (nums[38], nums[52])
    missing_sum = sum(set(range(a + 1, b)) - set(nums[38:53]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]