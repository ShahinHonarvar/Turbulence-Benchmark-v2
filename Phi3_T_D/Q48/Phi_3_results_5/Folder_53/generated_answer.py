def return_binary_or_hexa(nums):
    a = nums[200]
    b = nums[202]
    if a >= b:
        return ''
    missing_sum = sum(set(range(a + 1, b)) - set(nums[200:203])) if a != b else 0
    return bin(missing_sum).replace('0b', '') if missing_sum % 2 else hex(missing_sum)[2:]