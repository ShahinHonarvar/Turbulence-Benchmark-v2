def return_binary_or_hexa(nums):
    a = nums[69]
    b = nums[97]
    total = sum(range(a + 1, b))
    missing = [i for i in range(a + 1, b) if i not in nums[69:98]]
    if missing == list(range(a + 1, b)):
        return ''
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()