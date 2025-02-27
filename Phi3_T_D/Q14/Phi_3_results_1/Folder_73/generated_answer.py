def find_second_smallest_num(numbers):
    start_index = 59
    end_index = 97
    valid_numbers = [n for i, n in enumerate(numbers) if start_index <= i <= end_index]
    if len(valid_numbers) < 2:
        return None
    first_smallest, second_smallest = (float('inf'), float('inf'))
    for num in valid_numbers:
        if num <= first_smallest:
            first_smallest, second_smallest = (num, first_smallest)
        elif first_smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None