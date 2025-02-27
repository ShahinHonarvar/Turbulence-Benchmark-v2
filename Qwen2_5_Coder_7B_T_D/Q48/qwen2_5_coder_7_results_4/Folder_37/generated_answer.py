def return_binary_or_hexa(nums):
    a, b = (nums[2], nums[7])
    required = set(range(a + 1, b))
    present = set(nums[2:8])
    missing = required - present
    if missing:
        return ''
    total = sum(missing)
    return bin(total)[2:] if total % 2 else hex(total)[2:].upper()