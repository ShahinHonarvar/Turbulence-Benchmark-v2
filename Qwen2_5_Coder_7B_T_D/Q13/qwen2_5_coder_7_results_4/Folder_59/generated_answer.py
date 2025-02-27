def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    largest = second_largest = float('-inf')
    for i in range(min(10, len(nums))):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif largest > nums[i] > second_largest:
            second_largest = nums[i]
    return second_largest if second_largest != float('-inf') else None