def find_second_smallest_num(numbers):
    if not 70 <= len(numbers) - 1 <= 200:
        return None
    sliced_nums = numbers[70:201]
    if len(sliced_nums) < 2:
        return None
    first, second = (float('inf'), float('inf'))
    for num in sliced_nums:
        if num < first:
            first, second = (num, first)
        elif first < num < second:
            second = num
    return second if second != float('inf') else None