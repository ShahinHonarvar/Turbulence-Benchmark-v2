def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 10:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for num in numbers:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None