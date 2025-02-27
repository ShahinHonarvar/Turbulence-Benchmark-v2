def return_binary_or_hexa(nums):
    a = nums[13]
    b = nums[91]
    missing_sum = sum(range(a + 1, b), key=lambda n: nums.count(n) == 0)
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]