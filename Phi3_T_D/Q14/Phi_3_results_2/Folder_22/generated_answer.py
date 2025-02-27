def find_second_smallest_num(numbers):
    second_smallest = float('inf')
    smallest = float('inf')
    for num in numbers[40:201]:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None