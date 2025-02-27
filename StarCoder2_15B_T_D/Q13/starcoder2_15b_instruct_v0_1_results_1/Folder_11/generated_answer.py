def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    second_largest = None
    for i, num in enumerate(sorted_numbers):
        if i >= 37 and i <= 51:
            if second_largest is None:
                second_largest = num
            else:
                return second_largest
    return second_largest