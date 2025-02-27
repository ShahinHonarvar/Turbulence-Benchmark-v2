def find_second_largest_num(numbers):
    slice_nums = numbers[10:101]
    if len(slice_nums) < 2:
        return None
    largest = max(slice_nums[0], slice_nums[1])
    second_largest = min(slice_nums[0], slice_nums[1])
    for num in slice_nums[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest