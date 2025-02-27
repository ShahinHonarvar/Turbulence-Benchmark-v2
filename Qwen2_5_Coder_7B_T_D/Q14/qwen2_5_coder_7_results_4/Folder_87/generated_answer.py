def find_second_smallest_num(numbers):
    if len(numbers) < 89:
        return None
    sub_list = numbers[22:89]
    if len(sub_list) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None