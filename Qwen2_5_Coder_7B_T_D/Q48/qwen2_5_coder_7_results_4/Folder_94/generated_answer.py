def return_binary_or_hexa(nums):
    a = nums[42]
    b = nums[87]
    missing_sum = sum(range(a + 1, b)) - sum(filter(lambda x: a < x < b, nums))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:].upper()
    else:
        return bin(missing_sum)[2:]