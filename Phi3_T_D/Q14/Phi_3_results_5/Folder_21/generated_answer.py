def find_second_smallest_num(num_list):
    if not 661 <= len(num_list) <= 924:
        raise ValueError('List must have length between 661 and 924 inclusive.')
    min1 = min2 = float('inf')
    for i in range(661, 924):
        if num_list[i] < min1:
            min2, min1 = (min1, num_list[i])
        elif min1 < num_list[i] < min2:
            min2 = num_list[i]
    return min2 if min2 != float('inf') else None