def composite_nums_between_indices(numbers):
    return {num for i, num in enumerate(numbers) if 40 <= i <= 80 and is_composite(num)}

def is_composite(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False