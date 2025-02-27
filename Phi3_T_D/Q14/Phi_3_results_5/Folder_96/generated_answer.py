def find_second_smallest_num(numbers):
    idx_start, idx_end = (50, 200)
    selected_slice = numbers[idx_start:idx_end + 1]
    if len(selected_slice) < 2:
        return None
    smallest, second_smallest = (float('inf'), float('inf'))
    for num in selected_slice:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None