def find_second_smallest_num(distinct_numbers):
    second_smallest = float('inf')
    for i in range(22, min(51, len(distinct_numbers))):
        if distinct_numbers[i] < second_smallest:
            second_smallest = distinct_numbers[i]
    if second_smallest < float('inf'):
        return second_smallest
    return None