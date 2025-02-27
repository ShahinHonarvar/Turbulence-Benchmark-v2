def find_second_smallest_num(numbers):
    relevant_numbers = sorted(numbers[62:79])
    if len(relevant_numbers) < 2:
        return None
    else:
        return relevant_numbers[1]