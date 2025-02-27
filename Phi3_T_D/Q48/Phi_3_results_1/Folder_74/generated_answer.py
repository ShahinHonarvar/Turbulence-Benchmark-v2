def return_binary_or_hexa(nums):
    a = nums[69] if len(nums) > 69 else None
    b = nums[97] if len(nums) > 97 else None
    if a is None or b is None or a >= b:
        return ''
    missing_numbers = {x for x in range(a + 1, b) if x not in nums[69:98]}
    total = sum(missing_numbers)
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]