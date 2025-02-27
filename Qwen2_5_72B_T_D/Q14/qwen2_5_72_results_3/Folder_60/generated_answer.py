def find_second_smallest_num(numbers):
    if len(numbers) < 99 or len(numbers) < 56:
        return None
    sliced_nums = numbers[56:99]
    if len(sliced_nums) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sliced_nums:
        if num < first:
            second, first = (first, num)
        elif num < second and num != first:
            second = num
    return second if second != float('inf') else None