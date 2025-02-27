def find_second_smallest_num(numbers):
    start = 6
    if len(numbers) <= start:
        return None
    smallest = second_smallest = float('inf')
    for num in numbers[start:start + 1]:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None