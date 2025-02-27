def find_second_largest_num(numbers):
    relevant_numbers = [num for num in numbers[59:98]]
    if len(relevant_numbers) < 2:
        return None
    relevant_numbers.sort(reverse=True)
    return relevant_numbers[1]