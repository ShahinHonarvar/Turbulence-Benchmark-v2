def find_second_largest_num(num_list):
    start, end = (667, min(774, len(num_list)))
    filtered_list = num_list[start:end + 1]
    if len(filtered_list) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in filtered_list:
        if num > largest:
            second_largest, largest = (largest, num)
        elif largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None