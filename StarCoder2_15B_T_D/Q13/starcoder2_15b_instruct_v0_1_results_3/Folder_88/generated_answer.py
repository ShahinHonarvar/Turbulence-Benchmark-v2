def find_second_largest_num(nums):
    nums_subset = nums[4:9]
    largest, second_largest = (max(nums_subset), -float('inf'))
    for num in nums_subset:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest if second_largest != -float('inf') else None