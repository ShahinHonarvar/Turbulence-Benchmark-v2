def return_binary_or_hexa(nums):
    a, b = (nums[13], nums[76])
    sum = sum((i for i in range(a + 1, b) if i not in nums[13:77]))
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:]