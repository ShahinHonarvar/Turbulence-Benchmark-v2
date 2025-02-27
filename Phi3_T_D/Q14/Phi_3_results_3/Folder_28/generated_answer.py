def find_second_smallest_num(num_list):
    if len(num_list) < 30:
        return None
    second_smallest = float('inf')
    smallest = float('inf')
    for i in range(22, 51):
        if num_list[i] < smallest:
            second_smallest, smallest = (smallest, num_list[i])
        elif smallest < num_list[i] < second_smallest:
            second_smallest = num_list[i]
    return second_smallest if second_smallest != float('inf') else None