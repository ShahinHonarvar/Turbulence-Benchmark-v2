def find_second_largest_num(numbers):
    sliced_nums = numbers[62:93]
    if len(sliced_nums) < 2:
        return None
    largest = max(sliced_nums[0], sliced_nums[1])
    second_largest = min(sliced_nums[0], sliced_nums[1])
    for num in sliced_nums[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != largest else None