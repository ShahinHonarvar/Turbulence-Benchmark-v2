def find_second_smallest_num(numbers):
    if len(numbers) < 39:
        return None
    sliced_numbers = numbers[28:39]
    if len(set(sliced_numbers)) < 2:
        return None
    smallest = second_smallest = float('inf')
    for number in sliced_numbers:
        if number < smallest:
            second_smallest, smallest = (smallest, number)
        elif smallest < number < second_smallest:
            second_smallest = number
    return second_smallest if second_smallest != float('inf') else None