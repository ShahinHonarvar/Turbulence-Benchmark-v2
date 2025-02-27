def find_second_smallest_num(numbers):
    start, end = (30, 87)
    if not (0 <= start < len(numbers) and 0 <= end < len(numbers)):
        return None
    slice_numbers = numbers[start:end + 1]
    if len(slice_numbers) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in slice_numbers:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None