def find_second_smallest_num(numbers):
    if len(numbers[56:99]) < 2:
        return None
    second_smallest_val = float('inf')
    smallest_val = float('inf')
    for num in numbers[56:99]:
        if num < smallest_val:
            second_smallest_val = smallest_val
            smallest_val = num
        elif smallest_val < num < second_smallest_val:
            second_smallest_val = num
    return second_smallest_val if second_smallest_val != float('inf') else None