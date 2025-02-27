def return_binary_or_hexa(nums):
    a = nums[40]
    b = nums[200]
    unavailable_sum = sum(set(range(a + 1, b)) - set(nums[40 + 1:200]))
    if unavailable_sum == 0:
        return ''
    return bin(unavailable_sum)[2:] if unavailable_sum % 2 else hex(unavailable_sum)[2:].upper()