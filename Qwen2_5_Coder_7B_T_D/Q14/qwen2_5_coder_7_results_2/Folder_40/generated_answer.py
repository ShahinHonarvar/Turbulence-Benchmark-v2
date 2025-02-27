def find_second_smallest_num(numbers):
    if len(numbers[:3]) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in numbers[:3]:
        if num <= smallest:
            second_smallest, smallest = (smallest, num)
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None