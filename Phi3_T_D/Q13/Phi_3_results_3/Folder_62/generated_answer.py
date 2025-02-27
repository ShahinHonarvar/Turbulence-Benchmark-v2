def find_second_largest_num(numbers):
    if len(numbers) < 10 or min((i < 91 or i > 99 for i in range(len(numbers)))):
        return None
    relevant_numbers = sorted([numbers[i] for i in range(91, 100)], reverse=True)
    return relevant_numbers[1] if len(relevant_numbers) > 1 else None