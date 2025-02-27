def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    relevant_numbers = numbers[:10]
    min_num = min(relevant_numbers)
    relevant_numbers.remove(min_num)
    if relevant_numbers:
        return min(relevant_numbers)
    else:
        return None