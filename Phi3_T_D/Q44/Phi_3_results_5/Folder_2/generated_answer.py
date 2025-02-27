def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(numbers):
    return {number for number in numbers[35:50] if is_composite(number)}