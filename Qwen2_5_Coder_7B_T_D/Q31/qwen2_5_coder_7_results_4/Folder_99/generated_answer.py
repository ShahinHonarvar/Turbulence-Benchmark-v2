def if_perfect_num(numbers):
    return sum((numbers[733] // i for i in range(1, numbers[733]))) == numbers[733] if len(numbers) > 733 else False