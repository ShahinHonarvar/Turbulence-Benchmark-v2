def return_binary_or_hexa(nums):
    a = nums[62]
    b = nums[96]
    full_set = set(range(a + 1, b))
    given_set = set(nums[63:96])
    diff = full_set - given_set
    summation = sum(diff)
    if not diff:
        return ''
    if summation % 2:
        return bin(summation)[2:]
    else:
        return hex(summation)[2:]