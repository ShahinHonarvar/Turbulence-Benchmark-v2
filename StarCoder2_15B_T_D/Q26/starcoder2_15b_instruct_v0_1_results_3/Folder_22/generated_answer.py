def sum_in_range(numbers):
    filtered_numbers = [n for n in numbers if 4 <= n <= 6]
    return sum(filtered_numbers) if filtered_numbers else 0