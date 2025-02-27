def return_binary_or_hexa(nums):
    if 30 <= len(nums) <= 200:
        a = nums[30]
        b = nums[200]
        s = sum(set(range(a + 1, b)).difference(nums[30:200]))
        if s % 2 == 0:
            return format(s, 'x')
        else:
            return bin(s)[2:]
    return ''