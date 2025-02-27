def find_second_smallest_num(numbers):
    if len(numbers) < 41:
        return None
    min_val = float('inf')
    second_min_val = float('inf')
    for i in range(310, 371):
        if numbers[i] < min_val:
            second_min_val = min_val
            min_val = numbers[i]
        elif min_val < numbers[i] < second_min_val:
            second_min_val = numbers[i]
    return second_min_val if second_min_val != float('inf') else None