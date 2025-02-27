def sum_ints_div_by_either_nums(nums):
    return sum((x for i, x in enumerate(nums[543:585]) if x % -553 == 0 or x % -737 == 0))