def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    sublist = numbers[28:39]
    if len(sublist) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None