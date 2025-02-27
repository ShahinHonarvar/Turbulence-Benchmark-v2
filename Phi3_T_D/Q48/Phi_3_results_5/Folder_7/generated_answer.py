def return_binary_or_hexa(nums):
    a = nums[10]
    b = nums[97]
    missing_sum = sum(set(range(a + 1, b)).difference(nums[10:98]))
    return bin(missing_sum)[2:] if missing_sum % 2 else f'{missing_sum:x}'