def find_second_smallest_num(numbers):
    sub_array = numbers[31:35]
    if len(sub_array) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_array:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None