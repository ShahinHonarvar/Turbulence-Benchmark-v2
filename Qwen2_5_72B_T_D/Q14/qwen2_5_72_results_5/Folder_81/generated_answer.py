def find_second_smallest_num(numbers):
    if len(numbers) < 101 or len(numbers) < 11:
        return None
    else:
        sliced_numbers = numbers[10:101]
        if len(sliced_numbers) < 2:
            return None
        first_smallest = min(sliced_numbers)
        sliced_numbers.remove(first_smallest)
        second_smallest = min(sliced_numbers)
        return second_smallest