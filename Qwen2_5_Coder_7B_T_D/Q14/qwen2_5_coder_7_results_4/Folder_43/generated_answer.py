def find_second_smallest_num(numbers):
    sublist = numbers[74:96]
    if len(sublist) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in sublist:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None