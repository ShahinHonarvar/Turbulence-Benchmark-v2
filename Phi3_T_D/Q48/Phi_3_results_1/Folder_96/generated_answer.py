def return_binary_or_hexa(nums):
    if not 50 <= len(nums) <= 200:
        return ''
    a, b = (nums[50], nums[200])
    missing_sum = sum(set(range(a + 1, b)).difference(nums[50:200]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]