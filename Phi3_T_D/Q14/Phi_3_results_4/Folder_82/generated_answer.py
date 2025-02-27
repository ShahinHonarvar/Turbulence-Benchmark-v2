def find_second_smallest_num(numbers):
    valid_numbers = numbers[20:201]
    if len(valid_numbers) < 2:
        return None
    second_smallest = float('inf')
    smallest = valid_numbers[0]
    for num in valid_numbers:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None