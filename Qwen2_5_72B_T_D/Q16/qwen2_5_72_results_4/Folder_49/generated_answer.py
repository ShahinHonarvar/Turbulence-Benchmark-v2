def sum_even_ints_inclusive(numbers):
    return sum(numbers[8:81:2]) if len(numbers) > 80 else sum((num for num in numbers[8:81] if num % 2 == 0))