def find_second_smallest_num(numbers):
    sub_list = numbers[62:100]
    if len(sub_list) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in sub_list:
        if num <= smallest:
            smallest, second_smallest = (num, smallest)
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None