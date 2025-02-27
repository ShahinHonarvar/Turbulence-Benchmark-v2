def gcf_two_nums(nums):
    if len(nums) < 2:
        return None
    if 300 >= len(nums) or 616 >= len(nums):
        return None
    smallest = min(nums[300], nums[616])
    for i in range(smallest, 1, -1):
        if nums[300] % i == 0 and nums[616] % i == 0:
            return i
    return None