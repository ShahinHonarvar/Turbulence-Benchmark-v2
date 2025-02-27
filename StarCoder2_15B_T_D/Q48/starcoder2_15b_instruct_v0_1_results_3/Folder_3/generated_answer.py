def return_binary_or_hexa(nums):
    a = nums[56]
    b = nums[88]
    sum_ = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum_ += i
    if sum_ % 2 == 1:
        return bin(sum_)[2:]
    else:
        return hex(sum_)[2:].upper()