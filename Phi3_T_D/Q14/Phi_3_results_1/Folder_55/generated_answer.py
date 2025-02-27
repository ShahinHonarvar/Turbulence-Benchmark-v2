def find_second_smallest_num(numbers):
    if len(numbers) <= 10:
        return None
    start_idx = 10
    second_smallest = float('inf')
    for num in numbers[start_idx:]:
        if num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None