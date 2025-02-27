def find_second_smallest_num(numbers):
    sliced_numbers = numbers[209:557]
    if len(sliced_numbers) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in sliced_numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None