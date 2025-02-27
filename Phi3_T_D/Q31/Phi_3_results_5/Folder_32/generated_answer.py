def if_perfect_num(nums: list) -> bool:
    try:
        return sum([i for i in range(1, nums[849]) if nums[849] % i == 0]) == nums[849]
    except IndexError:
        return False