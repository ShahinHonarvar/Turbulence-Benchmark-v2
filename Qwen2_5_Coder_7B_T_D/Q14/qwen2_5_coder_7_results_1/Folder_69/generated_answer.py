def find_second_smallest_num(numbers):
    sub_list = numbers[25:88]
    if len(sub_list) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_list:
        if num < smallest:
            second_smallest, smallest = (smallest, num)
        elif smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None