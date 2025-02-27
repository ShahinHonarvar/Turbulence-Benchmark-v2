def find_second_largest_num(numbers):
    first_largest, second_largest = (float('-inf'), float('-inf'))
    for num in numbers[:2]:
        if num > first_largest:
            first_largest, second_largest = (num, first_largest)
        elif first_largest > num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else None