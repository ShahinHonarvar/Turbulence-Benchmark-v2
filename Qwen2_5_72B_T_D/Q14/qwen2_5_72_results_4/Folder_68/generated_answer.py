def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sliced_numbers = numbers[:9]
    min_num = min(sliced_numbers)
    second_min = float('inf')
    for num in sliced_numbers:
        if min_num < num < second_min:
            second_min = num
    return second_min if second_min != float('inf') else None